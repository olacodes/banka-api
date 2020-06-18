from rest_framework import serializers
from ..models.account import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.account_number = validated_data.get('account_number', instance.account_number)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.account_type = validated_data.get('account_type', instance.account_type)
        instance.account_status = validated_data.get('account_status', instance.account_status)
        instance.account_balance = validated_data.get('balance', instance.balance)

        instance.save()
        return instance
