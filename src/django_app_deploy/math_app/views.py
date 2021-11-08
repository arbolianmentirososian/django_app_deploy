from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class HelloView(APIView):
    """
    View for the hello function.
    """

    def get(self, request):
        """ Test function that returns string 'Hello, world!'.
        It can be used to check whether application is running.
        """
        return Response(data="Hello, world!\n", status=status.HTTP_200_OK)


class AddView(APIView):
    """
    View for the add function.
    """

    def get(self, request, num1, num2):
        """Calculates the sum of two integer numbers passed into the function.

        Parameters
        ----------
            num1: int
                The first number.
            num2: int
                The second number.

        Returns
        -------
            JSON
                JSON containing values of passed in numbers and their sum.
        """
        response = {
            "num1": num1,
            "num2": num2,
            "num1 + num2": num1 + num2
        }
        return Response(data=response, status=status.HTTP_200_OK)


class SubtractView(APIView):
    """
    View for the subtract function.
    """

    def get(self, request, num1, num2):
        """Calculates the difference of two integer numbers passed into the function.

        Parameters
        ----------
            num1: int
                The first number.
            num2: int
                The second number.

        Returns
        -------
            JSON
                JSON containing values of passed in numbers and their difference.
        """
        response = {
            "num1": num1,
            "num2": num2,
            "num1 - num2": num1 - num2
        }
        return Response(data=response, status=status.HTTP_200_OK)


class MultiplyView(APIView):
    """
    View for the multiply function.
    """

    def get(self, request, num1, num2):
        """Calculates the product of two integer numbers passed into the function.

        Parameters
        ----------
            num1: int
                The first number.
            num2: int
                The second number.

        Returns
        -------
            JSON
                JSON containing values of passed in numbers and their product.
        """
        response = {
            "num1": num1,
            "num2": num2,
            "num1 * num2": num1 * num2,
        }
        return Response(data=response, status=status.HTTP_200_OK)


class DivideView(APIView):
    """
    View for the divide function.
    """

    def get(self, request, num1, num2):
        """Calculates the quotient of two integer numbers passed into the function.

        Parameters
        ----------
            num1: int
                The first number.
            num2: int
                The second number.

        Returns
        -------
            JSON
                JSON containing values of passed in numbers and their quotient.
        """
        response = {
            "num1": num1,
            "num2": num2,
            "num1 / num2": num1 / num2,
        }
        return Response(data=response, status=status.HTTP_200_OK)


class ModuloView(APIView):
    """
    View for the modulo function.
    """

    def get(self, request, num1, num2):
        """Calculates the remainder of division of two integer numbers passed into the function.

        Parameters
        ----------
        num1: int
            The first number.
        num2: int
            The second number.

        Returns
        -------
            JSON
                JSON response with values of passed in numbers and the remainder of their division.

        """
        response = {
            "num1": num1,
            "num2": num2,
            "num1 % num2": num1 % num2,
        }
        return Response(data=response, status=status.HTTP_200_OK)