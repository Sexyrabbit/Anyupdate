from django.db import models

# Create your models here.

class Application(models.Model):
    app_name = models.CharField(max_length=50, unique=True, primary_key=True)
    Posx = models.IntegerField(null=True, blank=True)
    Posy = models.IntegerField(null=True, blank=True)
    Colspan = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "Application: {}".format(self.app_name)


class ConfigItem(models.Model):
    ci = models.CharField(max_length=50, unique=True, primary_key=True)
    app = models.ForeignKey(Application, related_name="configitem", on_delete=models.DO_NOTHING)

    def __str__(self):
        return "ConfigItem: {}".format(self.ci)


class Incident(models.Model):
    inc_id = models.CharField(max_length=50, unique=True, primary_key=True)
    short_desc = models.TextField(blank=True, max_length=500)
    configitem = modelsForeignKey(ConfigItem, related_name="incs", on_delete=models.DO_NOTHING)
    parent = models.CharField(null=True, max_length=100, blank=True)
    children = models.CharField(null=True, max_length=500, blank=True)

    def __str__(self):
        return "Incident: {}".format(self.inc_id)
