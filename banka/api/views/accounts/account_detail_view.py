from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

from ...models.account import Account
from ...utils.api_response import APIResponse
from ...serializers.account_serializer import AccountSerializer


class AccountDetail(APIView):
    def get_object(self, account_number):
        try:
            return Account.objects.get(account_number=account_number)
        except Account.DoesNotExist:
            raise Http404

    def put(self, request, account_number, format=None):

        account = self.get_object(account_number)
        print(account.balance)

        serializer = AccountSerializer(
            instance=account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res_data = serializer.data
            return Response({
                "status": 200,
                "data": {
                    "account_number": res_data["account_number"],
                    "account_status": res_data["account_status"],
                    "account_type": res_data["account_type"],
                    "balance": res_data['balance']
                }
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, account_number, format=None):
        account = self.get_object(account_number)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
