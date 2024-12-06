from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.viewsets import (
    BrokerageInvestmentConfigViewSet,
    BrokerageInvestmentTemplateViewSet,
    CashConfigViewSet,
    CashTemplateViewSet,
    DebtConfigViewSet,
    DebtTemplateViewSet,
    ExpenseConfigViewSet,
    ExpenseTemplateViewSet,
    IncomeConfigViewSet,
    IncomeTemplateViewSet,
    IraInvestmentConfigViewSet,
    IraInvestmentTemplateViewSet,
    RetirementConfigViewSet,
    RetirementTemplateViewSet,
    TaxConfigViewSet,
    TaxTemplateViewSet,
    TaxDeferredInvestmentConfigViewSet,
    TaxDeferredInvestmentTemplateViewSet,
    PlanConfigViewSet,
    PlanTemplateViewSet,
)

router = DefaultRouter()
router.register(r'brokerage-investment-configs', BrokerageInvestmentConfigViewSet)
router.register(r'brokerage-investment-templates', BrokerageInvestmentTemplateViewSet)
router.register(r'cash-configs', CashConfigViewSet)
router.register(r'cash-templates', CashTemplateViewSet)
router.register(r'debt-configs', DebtConfigViewSet)
router.register(r'debt-templates', DebtTemplateViewSet)
router.register(r'expense-configs', ExpenseConfigViewSet)
router.register(r'expense-templates', ExpenseTemplateViewSet)
router.register(r'income-configs', IncomeConfigViewSet)
router.register(r'income-templates', IncomeTemplateViewSet)
router.register(r'ira-investment-configs', IraInvestmentConfigViewSet)
router.register(r'ira-investment-templates', IraInvestmentTemplateViewSet)
router.register(r'retirement-configs', RetirementConfigViewSet)
router.register(r'retirement-templates', RetirementTemplateViewSet)
router.register(r'tax-configs', TaxConfigViewSet)
router.register(r'tax-templates', TaxTemplateViewSet)
router.register(r'tax-deferred-investment-configs', TaxDeferredInvestmentConfigViewSet)
router.register(r'tax-deferred-investment-templates', TaxDeferredInvestmentTemplateViewSet)
router.register(r'plan-configs', PlanConfigViewSet)
router.register(r'plan-templates', PlanTemplateViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('users/', include('django.contrib.auth.urls', )),
    path('', include(router.urls))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
