from django.contrib import admin
from plasma_donor_lists.models import( 
    A_PositiveDonorList,
    A_NegativeDonorList,
    B_PositiveDonorList,
    B_NegativeDonorList,
    AB_PositiveDonorList,
    AB_NegativeDonorList,
    O_PositiveDonorList,
    O_NegativeDonorList
    
)
admin.site.register(A_PositiveDonorList)
admin.site.register(A_NegativeDonorList)
admin.site.register(B_PositiveDonorList)
admin.site.register(B_NegativeDonorList)
admin.site.register(AB_PositiveDonorList)
admin.site.register(AB_NegativeDonorList)
admin.site.register(O_PositiveDonorList)
admin.site.register(O_NegativeDonorList)
