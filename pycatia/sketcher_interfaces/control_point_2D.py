#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""


class ControlPoint2D(Point2D):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SketcherInterfaces.GeometricElement
                |                         SketcherInterfaces.Geometry2D
                |                             SketcherInterfaces.Point2D
                |                                 ControlPoint2D
                | 
                | Class defining a spline control point in 2D Space.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.control_point2_d = com_object

    @property
    def curvature(self) -> float:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property Curvature() As double
                | 
                |     Returns the curvature properties of the spline control
                |     point
                | 
                |     Parameters:
                | 
                |         oCurvature
                |             The curvature of the tangent determined at the control
                |             point

        :return: float
        :rtype: float
        """

        return self.control_point2_d.Curvature

    @curvature.setter
    def curvature(self, value: float):
        """
        :param float value:
        """

        self.control_point2_d.Curvature = value

    def get_tangent(self, o_tangent: tuple) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetTangent(CATSafeArrayVariant oTangent)
                | 
                |     Returns the tangent properties of the spline control point
                | 
                |     Parameters:
                | 
                |         oTangent[0]
                |             The X Coordinate of the tangent determined at the control point
                |             
                |         oTangent[1]
                |             The Y Coordinate of the tangent determined at the control
                |             point

        :param tuple o_tangent:
        :return: None
        :rtype: None
        """
        return self.control_point2_d.GetTangent(o_tangent)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_tangent'
        # # vba_code = """
        # # Public Function get_tangent(control_point2_d)
        # #     Dim oTangent (2)
        # #     control_point2_d.GetTangent oTangent
        # #     get_tangent = oTangent
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_tangent(self, i_tangent_x: float, i_tangent_y: float) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetTangent(double iTangentX,
                | double iTangentY)
                | 
                |     Imposes the tangent properties of the spline control point
                | 
                |     Parameters:
                | 
                |         iTangentX
                |             The X Coordinate of the tangent determined at the control point
                |             
                |         iTangentY
                |             The Y Coordinate of the tangent determined at the control
                |             point

        :param float i_tangent_x:
        :param float i_tangent_y:
        :return: None
        :rtype: None
        """
        return self.control_point2_d.SetTangent(i_tangent_x, i_tangent_y)

    def unset_curvature(self) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub UnsetCurvature()
                | 
                |     Unsets the curvature properties of the spline control point

        :return: None
        :rtype: None
        """
        return self.control_point2_d.UnsetCurvature()

    def unset_tangent(self) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub UnsetTangent()
                | 
                |     Unsets the tangent properties of the spline control point

        :return: None
        :rtype: None
        """
        return self.control_point2_d.UnsetTangent()

    def __repr__(self):
        return f'ControlPoint2D(name="{ self.name }")'
