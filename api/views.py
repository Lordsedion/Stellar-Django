from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import generics
from .models import TextDefault
from .serializers import *
from rest_framework import status
from rest_framework .views import APIView
import requests
import fitz
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .serializers import UserLoginSerializer

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)

        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
        })


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            # print(f"Hello {user}")
            if user.is_active():
                # print("Active")
                login(request, user)
                return Response({"success": "Success"})
        return HttpResponse(f"User does not exist {username} {password}")


def main(request):
    return HttpResponse("<h1 class='bg-color '>The sky is bright interim</h1>")

class TextDefaultView(generics.CreateAPIView):
    queryset = TextDefault.objects.all()
    serializer_class = TextSerializer


def generate_id():
    length = 20
    while True:
        id = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase +string.digits, k=length))
        if TextDefault.objects.filter(rec=id).count() == 0:
            break
    return id


def save_audio(audio_data, file_path):
    with open(file_path, 'wb') as f:
        f.write(audio_data)

        
names = ['v2/en_speaker_0', 'v2/en_speaker_1', 'v2/en_speaker_2', 'v2/en_speaker_3', 'v2/en_speaker_4',
          'v2/en_speaker_5', 'v2/en_speaker_6', 'v2/en_speaker_7', 'v2/en_speaker_8', 'v2/en_speaker_9',
            'v2/zh_speaker_0', 'v2/zh_speaker_1', 'v2/zh_speaker_2', 'v2/zh_speaker_3', 'v2/zh_speaker_4', 
            'v2/zh_speaker_5', 'v2/zh_speaker_6', 'v2/zh_speaker_7', 'v2/zh_speaker_8', 'v2/zh_speaker_9', 
            'v2/fr_speaker_0', 'v2/fr_speaker_1', 'v2/fr_speaker_2', 'v2/fr_speaker_3', 'v2/fr_speaker_4', 
            'v2/fr_speaker_5', 'v2/fr_speaker_6', 'v2/fr_speaker_7', 'v2/fr_speaker_8', 'v2/fr_speaker_9', 
            'v2/de_speaker_0', 'v2/de_speaker_1', 'v2/de_speaker_2', 'v2/de_speaker_3', 'v2/de_speaker_4', 
            'v2/de_speaker_5', 'v2/de_speaker_6', 'v2/de_speaker_7', 'v2/de_speaker_8', 'v2/de_speaker_9', 
            'v2/hi_speaker_0', 'v2/hi_speaker_1', 'v2/hi_speaker_2', 'v2/hi_speaker_3', 'v2/hi_speaker_4',
              'v2/hi_speaker_5', 'v2/hi_speaker_6', 'v2/hi_speaker_7', 'v2/hi_speaker_8', 'v2/hi_speaker_9', 
              'v2/it_speaker_0', 'v2/it_speaker_1', 'v2/it_speaker_2', 'v2/it_speaker_3', 'v2/it_speaker_4', 
              'v2/it_speaker_5', 'v2/it_speaker_6', 'v2/it_speaker_7', 'v2/it_speaker_8', 'v2/it_speaker_9', 
              'v2/ja_speaker_0', 'v2/ja_speaker_1', 'v2/ja_speaker_2', 'v2/ja_speaker_3', 'v2/ja_speaker_4', 
              'v2/ja_speaker_5', 'v2/ja_speaker_6', 'v2/ja_speaker_7', 'v2/ja_speaker_8', 'v2/ja_speaker_9', 
              'v2/ko_speaker_0', 'v2/ko_speaker_1', 'v2/ko_speaker_2', 'v2/ko_speaker_3', 'v2/ko_speaker_4', 
              'v2/ko_speaker_5', 'v2/ko_speaker_6', 'v2/ko_speaker_7', 'v2/ko_speaker_8', 'v2/ko_speaker_9', 
              'v2/pl_speaker_0', 'v2/pl_speaker_1', 'v2/pl_speaker_2', 'v2/pl_speaker_3', 'v2/pl_speaker_4', 
              'v2/pl_speaker_5', 'v2/pl_speaker_6', 'v2/pl_speaker_7', 'v2/pl_speaker_8', 'v2/pl_speaker_9', 
              'v2/pt_speaker_0', 'v2/pt_speaker_1', 'v2/pt_speaker_2', 'v2/pt_speaker_3', 'v2/pt_speaker_4', 
              'v2/pt_speaker_5', 'v2/pt_speaker_6', 'v2/pt_speaker_7', 'v2/pt_speaker_8', 'v2/pt_speaker_9', 
              'v2/ru_speaker_0', 'v2/ru_speaker_1', 'v2/ru_speaker_2', 'v2/ru_speaker_3', 'v2/ru_speaker_4', 
              'v2/ru_speaker_5', 'v2/ru_speaker_6', 'v2/ru_speaker_7', 'v2/ru_speaker_8', 'v2/ru_speaker_9', 
              'v2/es_speaker_0', 'v2/es_speaker_1', 'v2/es_speaker_2', 'v2/es_speaker_3', 'v2/es_speaker_4', 
              'v2/es_speaker_5', 'v2/es_speaker_6', 'v2/es_speaker_7', 'v2/es_speaker_8', 'v2/es_speaker_9', 
              'v2/tr_speaker_0', 'v2/tr_speaker_1', 'v2/tr_speaker_2', 'v2/tr_speaker_3', 'v2/tr_speaker_4', 
              'v2/tr_speaker_5', 'v2/tr_speaker_6', 'v2/tr_speaker_7', 'v2/tr_speaker_8', 'v2/tr_speaker_9']


names_dict = {i: j for i,j in enumerate(names)}

def write_bytesio_to_txt(bytes_io, file_path):
    bytes_io.seek(0)
    data = bytes_io.getvalue()
    with open(file_path, 'wb') as txt_file:
        txt_file.write(data)


def write_bytesio_to_pdf(bytes_io, file_path):
    # Rewind the BytesIO object to the beginning

    bytes_io.seek(0)

    # Read the bytes data from the BytesIO object
    data = bytes_io.getvalue()

    # Write the bytes data to a text file
    with open(file_path, 'wb') as txt_file:
        txt_file.write(data)



def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()

    doc.close()
    return text

def get_file_suffix(file_path):
    """
    Get the suffix (file extension) of a file path.
    
    Parameters:
    - file_path (str): The file path from which to extract the suffix.
    
    Returns:
    - str: The suffix (including the dot) of the file, or an empty string if no suffix is found.
    """
    if '.' in file_path:
        return file_path.rsplit('.', 1)[-1]
    else:
        return ''


class CreateFileView(APIView):
    serializer_class = CreateFileSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        # print(f'Hard life: {str(request.FILES["text_file"])} {type(request.FILES["text_file"])} {request.FILES["text_file"].file}')
        file_type = get_file_suffix(str(request.FILES["text_file"]))

        if serializer.is_valid():
            id = generate_id()
            name = serializer.data["name"]
            file = request.FILES["text_file"]
            speaker = serializer.data["speaker"]
            

            print(serializer.data)

            file_content = ""
            if file_type == "txt":
                file_content = write_bytesio_to_txt(request.FILES["text_file"].file, f'api/assets/general/audio/{id}.txt')
            elif file_type == "pdf":
                write_bytesio_to_pdf(request.FILES["text_file"].file, file_path=f'api/assets/general/audio/{id}.pdf')
                file_content = extract_text_from_pdf(f'api/assets/general/audio/{id}.pdf')

            print(file_content)

            queryset = FileDefault.objects.filter(rec=id)
            if queryset.exists():
                text_file = queryset[0]
                text_file.name = name
                text_file.text_file = file,
                text_file.speaker = int(speaker)
                text_file.save()
            else:
                text_file = FileDefault(rec = id, name=name, text_file=f'api/assets/general/audio/{id}.{file_type}', speaker=speaker)
                text_file.save()
                print("Its mine!!!")
            
            url = "https://a54e-34-170-238-140.ngrok-free.app/predict"
            data = {
                "text": file_content[:50].replace("'", ""),
                "speaker": names_dict[speaker],
                "name": name,
                "id": id
                }
            response = requests.post(url, data=data)

            audio_file = None
            if response.status_code == 200:
                audio_data = response.content

                with open(f'api/assets/general/audio/{id}.wav', 'wb') as f:
                    f.write(audio_data)
                    audio_file = HttpResponse(audio_data, content_type='audio/wav', )
                    audio_file['Content-Disposition'] = f'attachment; filename="{id}.wav"'
                    # audio_file["text"] = file_content[:50].strip("\n")
                print("Audio file saved successfully!")
            else:
                print(f"Error: {response.status_code} - {response.reason}")

            if audio_file != None:
                return audio_file
            
            return Response(CreateFileSerializer(text_file).data, status=status.HTTP_200_OK)

        return Response({'message': "UnSuccessful"})


class CreateTextView(APIView):
    serializer_class = CreateTextSerializer
    permission_classes = [AllowAny] 

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.data["name"]
            text = serializer.data["text"]
            speaker = serializer.data["speaker"]
            id = generate_id()
            queryset = TextDefault.objects.filter(rec=id)
            
            if queryset.exists():
                audio = queryset[0]
                audio.name = name
                audio.text = text,
                audio.speaker = int(speaker)
                audio.save()
            else:
                audio = TextDefault(rec = id, name=name, text=text, speaker=speaker)
                audio.save()
            
            url = "https://ffce-35-192-26-225.ngrok-free.app/predict"
            data = {
                "text": text,
                "speaker": names_dict[speaker],
                "name": name,
                "id": id
                }
            response = requests.post(url, data=data)

            audio_file = None
            if response.status_code == 200:
                audio_data = response.content

                with open(f'api/assets/general/audio/{id}.wav', 'wb') as f:
                    f.write(audio_data)
                    audio_file = HttpResponse(audio_data, content_type='audio/wav', )
                    audio_file['Content-Disposition'] = f'attachment; filename="{id}.wav"'
                    audio_file["text"] = text
                print("Audio file saved successfully!")
            else:
                print(f"Error: {response.status_code} - {response.reason}")

            if audio_file != None:
                return audio_file
            
            return Response(TextSerializer(audio).data, status=status.HTTP_200_OK)

        else:
            print(f"Serializer Invalid { serializer}{serializer.data}")
            return Response("Error in request, Invalid format")
