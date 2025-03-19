from rest_framework import serializers


def check_divide_by_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError("10で割り切れる値にして下さい")


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    price = serializers.IntegerField(min_value=0)
    discounted_price = serializers.IntegerField(min_value=0, validators = [check_divide_by_ten])

    def validate_price(self, value):
        print(value)
        if value % 10 != 0:
            raise serializers.ValidationError("1桁目は０にして下さい")
        return value

    def validate_name(self, value):
        print({value})
        if value[0].islower():
            raise serializers.ValidationError("最初の文字は大文字にして下さい")
        return value

    def validate(self, data):
        print(data)
        price = data.get("price")
        discounted_price = data.get("discounted_price")
        if price < discounted_price:
            raise serializers.ValidationError(
                "割引価格は本来の価格以下の値にして下さい"
            )
        return data
