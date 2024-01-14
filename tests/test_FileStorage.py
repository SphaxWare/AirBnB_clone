import unittest
from models.base_model import BaseModel
from datetime import datetime
import json


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str(self):
        my_model = BaseModel()
        string = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), string)

    def test_save(self):
        my_model = BaseModel()
        updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(updated_at, my_model.updated_at)

    def test_to_dict(self):
        my_model = BaseModel()
        model_dict = my_model.to_dict()

        self.assertIsInstance(model_dict['id'], str)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_reload(self):
        my_model = BaseModel()
        my_model.save()

        my_model_dict = my_model.to_dict()
        my_model.reload()

        reloaded_model = BaseModel(**my_model_dict)

        # Check if attributes are the same
        self.assertEqual(my_model.id, reloaded_model.id)
        self.assertEqual(my_model.created_at, reloaded_model.created_at)
        self.assertEqual(my_model.updated_at, reloaded_model.updated_at)

        # Check if objects are not the same
        self.assertIsNot(my_model, reloaded_model)


if __name__ == '__main__':
    unittest.main()
