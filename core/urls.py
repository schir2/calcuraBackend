from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.serializers import CommandSerializer, CommandSequenceSerializer, CommandSequenceCommandSerializer
from main.views import login_view, logout_view, get_csrf_token
from main.viewsets import (
    BrokerageInvestmentViewSet,
    BrokerageInvestmentTemplateViewSet,
    CashReserveViewSet,
    CashReserveTemplateViewSet,
    DebtViewSet,
    DebtTemplateViewSet,
    ExpenseViewSet,
    ExpenseTemplateViewSet,
    IncomeViewSet,
    IncomeTemplateViewSet,
    IraInvestmentViewSet,
    IraInvestmentTemplateViewSet,
    TaxDeferredInvestmentViewSet,
    TaxDeferredInvestmentTemplateViewSet,
    PlanViewSet,
    PlanTemplateViewSet, RothIraInvestmentViewSet, RothIraInvestmentTemplateViewSet, UserViewSet,
    CommandSequenceCommandViewSet, CommandSequenceViewSet, CommandViewSet,
)

router = DefaultRouter()
router.register('brokerage-investments', BrokerageInvestmentViewSet, basename='brokerage-investment')
router.register('brokerage-investment-templates', BrokerageInvestmentTemplateViewSet, basename='brokerage-investment-template')
router.register('cash-reserves', CashReserveViewSet, basename='cash-reserve')
router.register('cash-reserve-templates', CashReserveTemplateViewSet, basename='cash-reserve-template')
router.register('debts', DebtViewSet, basename='debt')
router.register('debt-templates', DebtTemplateViewSet, basename='debt-template')
router.register('expenses', ExpenseViewSet, basename='expense')
router.register('expense-templates', ExpenseTemplateViewSet,basename='expense-template')
router.register('incomes', IncomeViewSet,basename='income')
router.register('income-templates', IncomeTemplateViewSet, basename='income-template')
router.register('ira-investments', IraInvestmentViewSet, basename='ira-investment')
router.register('ira-investment-templates', IraInvestmentTemplateViewSet, basename='ira-investment-template')
router.register('roth-ira-investments', RothIraInvestmentViewSet, basename='roth-ira-investment')
router.register('roth-ira-investment-templates', RothIraInvestmentTemplateViewSet, basename='roth-ira-investment-template')
router.register('tax-deferred-investments', TaxDeferredInvestmentViewSet, basename='tax-deferred-investment')
router.register('tax-deferred-investment-templates', TaxDeferredInvestmentTemplateViewSet, basename='tax-deferred-investment-template')
router.register('plans', PlanViewSet, basename='plan')
router.register('plan-templates', PlanTemplateViewSet, basename='plan-template')
router.register('commands', CommandViewSet, basename='command')
router.register('command-sequences', CommandSequenceViewSet, basename='command-sequence')
router.register('command-sequence-commands', CommandSequenceCommandViewSet, basename='command-sequence-command')
router.register('users', UserViewSet, basename='user')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('users/', include('django.contrib.auth.urls', )),
    path('api/', include(router.urls)),
    path("api/auth/login/", login_view, name="login"),
    path("api/auth/logout/", logout_view, name="logout"),
    path("api/auth/csrf/", get_csrf_token, name="csrf"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
