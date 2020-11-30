from django.shortcuts import render
from django.views import View
from django.http import HttpRequest
# Create your views here.

class ViewHomePage(View):
    template = 'index.html'
    def get(self, request):
        return render(request, self.template,{'title':'Alkhwarizmi','page':1})

class ViewSoftDev(View):
    template = 'softdev.html'
    def get(self,request):
        
        return render(request, self.template, {'title':'Alkhwarizmi','page':2.1})

class ViewCourseEvent(View):
    template ='course.html'
    def get(self, request,status =1):
        base_url = request.get_host()
        data = [            
            {'program':'Writting',
             'client_url':'#',
            'skills':['Mobile App','UI Design','Data Management'],
            'date':'13 - 9 - 20',
            'url':'https://play.google.com/store/apps/details?id=id.khwarizmi.qbsdonation',
            'detail':'An application for donating to be used in the field of tahfidzul Quran and information technology. Builded by flutter technology that will give a good performance & interactive UI for user.',
            'testimoni':"When the company's creative director approached me for this project, I knew it would be an awesome opportunity to create something unique. Here are more details",
            'icon':'http://'+base_url+'/static/images/icon_dafq.png'
            },
            {'program':'Illustration',
            'client_url':'http://sekolahimpian.com',
            'skills':['Game Development','2D Animation', 'UI Design'],
            'date':'13 - 9 - 20',
            'url':'https://play.google.com/store/apps/details?id=com.alkhwarizmi.nada',
            'detail':'A story telling game that tell to us how a student learn in islamic boarding school. Builded with unity that will make it fast to load in every device.',
            'testimoni':"When the company's creative director approached me for this project, I knew it would be an awesome opportunity to create something unique. Here are more details",
            'icon':'http://'+base_url+'/static/images/icon_nada.jpg'
            },
            {'program':'IOT',
            'client_url':'#',
            'skills':['Mobile Development','Network Organizer', 'UI Design'],
            'date':'13 - 9 - 20',
            'url':'https://play.google.com/store/apps/details?id=com.ndeztea.quranmemocommunity',
            'detail':"QuranMemo Community is a tool for memorizing Al-Quran combined with a social network with other Al-Quran memorizers, so that the memorizers of the Koran can correct each other's memorization.",
            'testimoni':"When the company's creative director approached me for this project, I knew it would be an awesome opportunity to create something unique. Here are more details",
            'icon':'http://'+base_url+'/static/images/icon_qas.jpg'
            }
            ]
        print(len(data))
        return render(request, self.template,{'title':'Alkhwarizmi','page':2.2,'status':status,'data':data[status],'total':len(data)})

class ViewImageVideo(View):
    template = 'imagevideo.html'
    def get(self, request):
        return render(request, self.template,{'title':'Alkhwarizmi','page':2.3})

class ViewProduct(View):
    template ='product.html'
    def get(self, request):
        return render(request, self.template,{'title':'Alkhwarizmi','page':3})

class ViewEvent(View):
    template= 'event.html'
    def get(self, request):
        return render(request, self.template,{'title':'Alkhwarizmi','page':4})

class ViewPortfolio(View):
    template = 'portfolio.html'
    def get(self, request, status=1):
        base_url = request.get_host()
        data = [            
            {'client':'Dompet Amal Fahim Quran',
             'client_url':'http://daf-q.id',
            'skills':['Mobile App','UI Design','Data Management'],
            'date':'13 - 9 - 20',
            'url':'https://play.google.com/store/apps/details?id=id.khwarizmi.qbsdonation',
            'detail':'An application for donating to be used in the field of tahfidzul Quran and information technology. Builded by flutter technology that will give a good performance & interactive UI for user.',
            'testimoni':"When the company's creative director approached me for this project, I knew it would be an awesome opportunity to create something unique. Here are more details",
            'icon':'http://'+base_url+'/static/images/icon_dafq.png'
            },
            {'client':'Fahim Quran',
            'client_url':'http://sekolahimpian.com',
            'skills':['Game Development','2D Animation', 'UI Design'],
            'date':'13 - 9 - 20',
            'url':'https://play.google.com/store/apps/details?id=com.alkhwarizmi.nada',
            'detail':'A story telling game that tell to us how a student learn in islamic boarding school. Builded with unity that will make it fast to load in every device.',
            'testimoni':"When the company's creative director approached me for this project, I knew it would be an awesome opportunity to create something unique. Here are more details",
            'icon':'http://'+base_url+'/static/images/icon_nada.jpg'
            },
            {'client':'Bandung Tahfidz',
            'client_url':'#',
            'skills':['Mobile Development','Network Organizer', 'UI Design'],
            'date':'13 - 9 - 20',
            'url':'https://play.google.com/store/apps/details?id=com.ndeztea.quranmemocommunity',
            'detail':"QuranMemo Community is a tool for memorizing Al-Quran combined with a social network with other Al-Quran memorizers, so that the memorizers of the Koran can correct each other's memorization.",
            'testimoni':"When the company's creative director approached me for this project, I knew it would be an awesome opportunity to create something unique. Here are more details",
            'icon':'http://'+base_url+'/static/images/icon_qas.jpg'
            }
            ]
        
        return render(request, self.template,{'title':'Alkhwarizmi','page':2.1,'status':status,'data':data[status],'total':len(data)})
