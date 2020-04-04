from django.db import models

class Startdata(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

class Metadata(models.Model):
    research_phase_number = models.CharField(max_length=30)
    research_phases30 = models.CharField(max_length=30)
    research_phases7 = models.CharField(max_length=30)

class ToolsAndInnovations(models.Model):
    name = models.CharField(max_length=30, help_text="name (blue ones were added during last update)")
    url = models.CharField(max_length=30, help_text="clickable link")
    web_launchyear = models.IntegerField(help_text="year of weblaunch / introduction / founding")
    prime_phase_alpha = models.CharField(max_length=30, help_text="primary phase of workflow targeted")
    prime_phase_number = models.IntegerField(help_text="phase order")
    function_free = models.TextField(max_length=1000, help_text="what is/does it? (free text)")
    ui_functionfree = models.CharField(max_length=30, help_text="user input for what is/does it?")
    function_controlled = models.CharField(max_length=30, help_text="what is/does it? (controlled)")
    geo_category = models.CharField(max_length=30, help_text="open / efficient / good")
    ui_geo_category = models.CharField(max_length=30, help_text="Does the tool make science more open, efficient or good / reproducible?")
    twitter = models.CharField(max_length=30)
    twitter_follow_latest = models.IntegerField(help_text="Twitter followers")
    active_pre = models.CharField(max_length=30, help_text="preparation / define research priorities / get funding")
    active_dis = models.CharField(max_length=30, help_text="discovery, data collection")
    active_ana = models.CharField(max_length=30, help_text="analysis")
    active_wri = models.CharField(max_length=30, help_text="authoring / writing / including annotations")
    active_pub = models.CharField(max_length=30, help_text="publication / archiving / sharing")
    active_out = models.CharField(max_length=30, help_text="outreach & visibility")
    active_ass = models.CharField(max_length=30, help_text="assessment / metrics (incl. comments, discussion)")

class Recommendations(models.Model):
    creators_title = models.CharField(max_length=30)
    link = models.CharField(max_length=100)


