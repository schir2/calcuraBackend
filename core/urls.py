from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested.routers import NestedDefaultRouter, DefaultRouter

from main.viewsets import (
    BrokerageViewSet,
    BrokerageTemplateViewSet,
    CashReserveViewSet,
    CashReserveTemplateViewSet,
    DebtViewSet,
    DebtTemplateViewSet,
    ExpenseViewSet,
    ExpenseTemplateViewSet,
    IncomeViewSet,
    IncomeTemplateViewSet,
    IraViewSet,
    IraTemplateViewSet,
    TaxDeferredViewSet,
    TaxDeferredTemplateViewSet,
    PlanViewSet,
    PlanTemplateViewSet, RothIraViewSet, RothIraTemplateViewSet, CommandSequenceCommandViewSet,
    CommandSequenceViewSet, CommandViewSet, HsaViewSet,
)
from users.views import login_view, logout_view, get_csrf_token, register_view, verify_view, email_exists_view
from users.viewsets import UserViewSet, ProfileViewSet

router = DefaultRouter()
router.register('brokerages', BrokerageViewSet, basename='brokerage')
router.register('cash-reserves', CashReserveViewSet, basename='cash-reserve')
router.register('debts', DebtViewSet, basename='debt')
router.register('expenses', ExpenseViewSet, basename='expense')
router.register('incomes', IncomeViewSet, basename='income')
router.register('iras', IraViewSet, basename='ira')
router.register('hsas', HsaViewSet, basename='hsa')
router.register('roth-iras', RothIraViewSet, basename='roth-ira')
router.register('tax-deferreds', TaxDeferredViewSet, basename='tax-deferred')
router.register('commands', CommandViewSet, basename='command')
router.register('command-sequences', CommandSequenceViewSet, basename='command-sequence')
router.register('command-sequence-commands', CommandSequenceCommandViewSet, basename='command-sequence-command')
router.register('plans', PlanViewSet, basename='plan')
router.register('users', UserViewSet, basename='user')
router.register('profiles', ProfileViewSet, basename='profile')

plan_router = NestedDefaultRouter(router, r'plans', lookup='plan')
plan_router.register(r'brokerages', BrokerageViewSet, basename='plan-brokerage')
plan_router.register(r'cash-reserves', CashReserveViewSet, basename='plan-cash-reserve')
plan_router.register(r'debts', DebtViewSet, basename='plan-debt')
plan_router.register(r'expenses', ExpenseViewSet, basename='plan-expense')
plan_router.register(r'incomes', IncomeViewSet, basename='plan-income')
plan_router.register(r'iras', IraViewSet, basename='plan-ira')
plan_router.register(r'roth-iras', RothIraViewSet, basename='plan-roth-ira')
plan_router.register(r'tax-deferreds', TaxDeferredViewSet, basename='plan-tax-deferred')


router.register('brokerage-templates', BrokerageTemplateViewSet,
                basename='brokerage-template')
router.register('cash-reserve-templates', CashReserveTemplateViewSet, basename='cash-reserve-template')
router.register('debt-templates', DebtTemplateViewSet, basename='debt-template')
router.register('expense-templates', ExpenseTemplateViewSet, basename='expense-template')
router.register('income-templates', IncomeTemplateViewSet, basename='income-template')
router.register('ira-templates', IraTemplateViewSet, basename='ira-template')
router.register('roth-ira-templates', RothIraTemplateViewSet,
                basename='roth-ira-template')
router.register('tax-deferred-templates', TaxDeferredTemplateViewSet,
                basename='tax-deferred-template')
router.register('plan-templates', PlanTemplateViewSet, basename='plan-template')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('users/', include('django.contrib.auth.urls', )),
    path('api/', include(router.urls)),
    path('api/', include(plan_router.urls)),
    path("api/auth/login/", login_view, name="login"),
    path("api/auth/logout/", logout_view, name="logout"),
    path("api/auth/register/", register_view, name="register"),
    path("api/auth/csrf-token/", get_csrf_token, name="csrf"),
    path("api/auth/verify/", verify_view, name="verify"),
    path("api/auth/email-exists/", email_exists_view, name="email-exists"),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
