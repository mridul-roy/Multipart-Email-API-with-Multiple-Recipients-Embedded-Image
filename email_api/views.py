from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMultiAlternatives
from .serializers import EmailSerializer
from .utils import is_valid_recipient

class SendEmailView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            recipients = data['recipients']
            if not all(is_valid_recipient(r) for r in recipients):
                return Response({
                    "status": "error",
                    "message": "Only Gmail, Hotmail, Yahoo, and careers@accelx.net are allowed"
                }, status=status.HTTP_400_BAD_REQUEST)

            screenshot = data['screenshot']
            image_content = screenshot.read()
            image_cid = 'screenshot_image'

            subject = f"Python Backend Engineer Selection Task - {data['name']}"
            html_body = f"""
            <html>
              <body style="font-family: Arial;">
                <h2>Candidate Details</h2>
                <p><strong>Name:</strong> {data['name']}</p>
                <p><strong>Education:</strong> {data['education']}</p>
                <p><strong>Contact:</strong> {data['contact']}</p>
                <p><strong>Address:</strong> {data['address']}</p>
                <div style="text-align:center; margin:20px 0;">
                  <img src="cid:{image_cid}" style="max-width:500px;" />
                </div>
                <h3>Project Idea</h3>
                <p>{data['project_idea']}</p>
              </body>
            </html>
            """

            msg = EmailMultiAlternatives(subject, "", to=recipients)
            msg.attach_alternative(html_body, "text/html")
            msg.attach(image_cid, image_content, screenshot.content_type)
            msg.content_subtype = 'html'
            msg.mixed_subtype = 'related'
            msg.send()

            return Response({
                "status": "success",
                "message": f"Email sent to {len(recipients)} recipients"
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
