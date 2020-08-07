def get_data(obj, serializer, dataList=[], context={}, many=False):
    nowFields = serializer.Meta.fields
    method_fields = ()
    if hasattr(serializer.Meta, 'method_fields'):
        method_fields = serializer.Meta.method_fields
    if not dataList:
        dataList = nowFields
    else:
        dataList = list(set(dataList) | set(method_fields))
    serializer.Meta.fields = dataList
    data = serializer(obj, context=context, many=many).data
    serializer.Meta.fields = nowFields
    return data
