# Serializers convert model instances to JSON so that the frontend can work with the received data

from rest_framework import serializers
from .models import Receipt, Item

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')


class ItemSerializer(serializers.ModelSerializer):
    #  https://stackoverflow.com/questions/37240621/django-rest-framework-updating-nested-objectav
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'receipt')

class ReceiptSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    
    class Meta:
        model = Receipt
        fields = ('id', 'tax', 'total', 'items', 'tip')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        receipt = Receipt.objects.create(**validated_data)
        for item_data in items_data:
            #TODO: Bulk insert?
            print(receipt)
            Item.objects.create(receipt=receipt, **item_data)
        return receipt

    def update(self, receipt, validated_data):
        items_data = validated_data.pop('items')
        print(items_data)
        receipt.tax = validated_data.get("tax", receipt.tax)
        receipt.total = validated_data.get("total", receipt.total)
        receipt.tip = validated_data.get("tip", receipt.tip)
        receipt.save()
        
        for item_data in items_data:
            print(item_data)
            item = Item.objects.get(pk=item_data['id'])
            item.name = item_data.get('name', item.name)
            item.price = item_data.get('price', item.price)
            item.save()
        return receipt