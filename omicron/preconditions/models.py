from django.db import models
from omicron.testcases.models import TestCase

class OmPrecondition(models.Model):
    precondition_id = models.AutoField(primary_key=True)
    test_case = models.ForeignKey(TestCase)

    def __unicode__(self):
        return str(self.precondition_id)
    
    class Meta:
        db_table = "om_pco_precondition"


class OmPreconditionTestCase(models.Model):
    precondition_test_case_id = models.AutoField(primary_key=True)
    test_case = models.ForeignKey(TestCase)
    precondition = models.ForeignKey(OmPrecondition)

    def __unicode__(self):
        return str(self.precondition_test_case_id)

    class Meta:
        unique_together = (("test_case", "precondition"),)
        db_table = "om_pco_precondition_test_case"


class OmPreconditionDescription(models.Model):
    precondition_description_id = models.AutoField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    precondition = models.ForeignKey(OmPrecondition)

    def __unicode__(self):
        return str(self.precondition_description_id)
        
    class Meta:
        db_table = "om_pco_precondition_description"