from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer

# class VendorViewSet(viewsets.ModelViewSet):
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer

# class PurchaseOrderListCreateAPIView(APIView):
#     def get(self, request):
#         vendor_id = request.query_params.get('vendor_id')
#         if vendor_id:
#             purchase_orders = PurchaseOrder.objects.filter(vendor__id=vendor_id)
#         else:
#             purchase_orders = PurchaseOrder.objects.all()

#         serializer = PurchaseOrderSerializer(purchase_orders, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PurchaseOrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PurchaseOrderRetrieveUpdateDestroyAPIView(APIView):
#     def get_purchase_order(self, po_id):
#         try:
#             return PurchaseOrder.objects.get(pk=po_id)
#         except PurchaseOrder.DoesNotExist:
#             return None

#     def get(self, request, po_id):
#         purchase_order = self.get_purchase_order(po_id)
#         if purchase_order:
#             serializer = PurchaseOrderSerializer(purchase_order)
#             return Response(serializer.data)
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, po_id):
#         purchase_order = self.get_purchase_order(po_id)
#         if purchase_order:
#             serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, po_id):
#         purchase_order = self.get_purchase_order(po_id)
#         if purchase_order:
#             purchase_order.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response(status=status.HTTP_404_NOT_FOUND)

class VendorListCreateAPIView(ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateAPIView(ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer