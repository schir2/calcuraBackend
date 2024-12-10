from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.viewsets import (
    BrokerageInvestmentViewSet,
    BrokerageInvestmentTemplateViewSet,
    CashViewSet,
    CashTemplateViewSet,
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
    PlanTemplateViewSet,
)

router = DefaultRouter()
router.register(r'brokerage-investments', BrokerageInvestmentViewSet)
router.register(r'brokerage-investment-templates', BrokerageInvestmentTemplateViewSet)
router.register(r'cashes', CashViewSet)
router.register(r'cash-templates', CashTemplateViewSet)
router.register(r'debts', DebtViewSet)
router.register(r'debt-templates', DebtTemplateViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'expense-templates', ExpenseTemplateViewSet)
router.register(r'incomes', IncomeViewSet)
router.register(r'income-templates', IncomeTemplateViewSet)
router.register(r'ira-investments', IraInvestmentViewSet)
router.register(r'ira-investment-templates', IraInvestmentTemplateViewSet)
router.register(r'tax-deferred-investments', TaxDeferredInvestmentViewSet)
router.register(r'tax-deferred-investment-templates', TaxDeferredInvestmentTemplateViewSet)
router.register(r'plans', PlanViewSet)
router.register(r'plan-templates', PlanTemplateViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('users/', include('django.contrib.auth.urls', )),
    path('api/', include(router.urls))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
