#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.funct_system_interfaces.functional_object import FunctionalObject
from pycatia.funct_system_interfaces.functional_object_proxy import FunctionalObjectProxy
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant

if TYPE_CHECKING:
    from pycatia.funct_system_interfaces.functional_description import FunctionalDescription


class FunctionalObjects(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     FunctionalObjects
                | 
                | Interface to access a collection of FunctionalObjects.
    
    """

    def __init__(self, com_object, child_object=FunctionalObject):
        super().__init__(com_object, child_object=FunctionalObject)
        self.functional_objects = com_object
        self.child_object = FunctionalObject

    def create(self, i_name: str) -> FunctionalObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Create(CATBSTR iName) As FunctionalObject
                | 
                |     Creates a FunctionalObject.

        :param str i_name:
        :return: FunctionalObject
        :rtype: FunctionalObject
        """
        return FunctionalObject(self.functional_objects.Create(i_name))

    def create_proxy(self, i_name: str, i_desc: 'FunctionalDescription') -> FunctionalObjectProxy:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func CreateProxy(CATBSTR iName,
                | FunctionalDescription iDesc) As FunctionalObjectProxy
                | 
                |     Creates a FunctionalObjectProxi.

        :param str i_name:
        :param FunctionalDescription i_desc:
        :return: FunctionalObjectProxy
        :rtype: FunctionalObjectProxy
        """
        return FunctionalObjectProxy(self.functional_objects.CreateProxy(i_name, i_desc.com_object))

    def delete(self, i_object: FunctionalObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Delete(FunctionalObject iObject)
                | 
                |     Deletes a FunctionalObject.

        :param FunctionalObject i_object:
        :return: None
        :rtype: None
        """
        return self.functional_objects.Delete(i_object.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'delete'
        # # vba_code = """
        # # Public Function delete(functional_objects)
        # #     Dim iObject (2)
        # #     functional_objects.Delete iObject
        # #     delete = iObject
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def elem(self, i_index: cat_variant) -> FunctionalObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Elem(CATVariant iIndex) As FunctionalObject
                | 
                |     Returns an action using its index or its name from the actions
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the action to retrieve from the collection
                |             of actions. As a numerics, this index is the rank of the action in the
                |             collection. The index of the first action in the collection is 1, and the index
                |             of the last action is Count. As a string, it is the name you assigned to the
                |             action using the 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved action 
                |     Example:
                |         This example retrieves in Obj1 the fifth object in the collection and
                |         in Obj2 the action named Valve.
                | 
                |          Dim Obj1 As FunctionalObject
                |          Set Obj1 = Desc.Object(5)
                |          Dim Obj2 As FunctionalObject
                |          Set Obj2 = Desc.Object("Valve")

        :param CATVariant i_index:
        :return: FunctionalObject
        :rtype: FunctionalObject
        """
        return FunctionalObject(self.functional_objects.Elem(i_index))

    def __repr__(self):
        return f'FunctionalObjects(name="{self.name}")'
