#! yusuke-hi-rei add start
'''
 ビューの作成
'''
from django.views import generic
from .forms import InquiryForm
#from django.shortcuts import render

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"

#! 問い合わせページ用のビュー
class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
#! yusuke-hi-rei add end
