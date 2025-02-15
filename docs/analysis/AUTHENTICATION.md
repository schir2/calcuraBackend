# Authentication Review

Below is a broad overview of your current authentication setup—covering security considerations, password handling, and potential improvements for a robust **session-based registration** flow. Let me know if you want more depth in any specific area!

---

## What Looks Solid

1. **Session Auth Flow**  
   - You use Django’s built-in `authenticate(request, username, password)` plus `login`/`logout` in `views.py`.  
   - Django session cookies handle session storage, which works well for your scenario.

2. **CSRF Protection**  
   - The `get_csrf_token` endpoint returns a token, and `login_view` is protected by `@csrf_protect`.  
   - Ensures your frontend can include the token for cross-site request forgery protection.

3. **DRF Viewsets**  
   - A `UserViewSet` with `UserSerializer` for CRUD operations on users.  
   - `password` is `write_only=True`, preventing it from leaking in responses.

4. **Admin vs. API Separation**  
   - You use Django’s admin for privileged local/GUI actions.  
   - The DRF endpoints expose JSON-based CRUD, typically restricted per user permissions.

---

## Potential Gaps & Improvements

### 1. **Password Hashing in Serializer**

- **What**: By default, DRF’s `ModelSerializer` might store passwords in plain text if you don’t explicitly call `set_password()`.  
- **Why**: The default `create` method does `User.objects.create(**validated_data)`, which bypasses Django’s hashing.  
- **How to Fix**: Override `create()` and `update()` in your serializer:
  ```python
  def create(self, validated_data):
      password = validated_data.pop('password', None)
      user = super().create(validated_data)
      if password:
          user.set_password(password)
          user.save()
      return user

  def update(self, instance, validated_data):
      password = validated_data.pop('password', None)
      user = super().update(instance, validated_data)
      if password:
          user.set_password(password)
          user.save()
      return user
