from django.contrib import admin
from Contest.models import Match, MatchSubmit, MatchRegister, MatchInclude, MatchRank

admin.site.site_header = 'Noob Dream 管理平台'
admin.site.site_title = 'Dream Judge'

admin.site.register(Match)
admin.site.register(MatchRegister)
admin.site.register(MatchSubmit)
admin.site.register(MatchInclude)
admin.site.register(MatchRank)

# Register your models here.
