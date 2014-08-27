from datetime import datetime

from django.test import TestCase

from kappa.requirements.models import Requirement
from shared.states_simplicity.models import State, StateType
from shared.types_simplicity.models import Type, TypeClassification


# MODELS
class RequirementTestCase(TestCase):
    
    def create_requirement(self):
        type_clasif_retrieved= TypeClassification.objects.create(type_classification_id=1, name="name", code="code")
        state_type_retrieved= StateType.objects.create(state_type_id=1, name="name", description="code")
        type_retrieved= Type.objects.create(type_id=1, name="name", code="code", type_classification=type_clasif_retrieved) 
        state_retrieved= State.objects.create(state_id=1, name="name", description="description", state_type=state_type_retrieved) 
        return Requirement.objects.create(title="Req_test", description="description example", type=type_retrieved, state=state_retrieved, 
                                   date_created=datetime.now(), date_modified=datetime.now(), code="123", 
                                   keywords="keyword1, keyword2", is_active="1")
        
    def test_requirement_creation(self):
        requirement_instance = self.create_requirement()
        self.assertTrue(isinstance(requirement_instance, Requirement))
        self.assertEqual(requirement_instance.__unicode__(), requirement_instance.title)