



#------发送HTML形式的邮件------#
# 需要使用到SMTPLIB库来进行邮箱的连接
import smtplib
# 处理邮件内容的库，email.mine
from email.mime.text import MIMEText
 
# 邮箱属性配置
 
# 邮箱服务端
mailserver = 'smtp.126.com'
# 发件人-填写自己的邮箱
userName_SendMail = 'rang13298112652@126.com'
# 邮箱发件授权码-为发件人生成的授权码
userName_AuthCode = 'LJJUZGDIYYETWBOA'
# 定义邮件的接收者-我随便写的，若收件人较多，可用列表表示
received_mail = ['xiongjianhao@airdoc.com']
 
# 发送一封HTML内容的邮件
content = """
<!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
  <title>
  </title>
  <!--[if !mso]><!-->
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <!--<![endif]-->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style type="text/css">
    #outlook a {
      padding: 0;
    }

    body {
      margin: 0;
      padding: 0;
      -webkit-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
    }

    table,
    td {
      border-collapse: collapse;
      mso-table-lspace: 0pt;
      mso-table-rspace: 0pt;
    }

    img {
      border: 0;
      height: auto;
      line-height: 100%;
      outline: none;
      text-decoration: none;
      -ms-interpolation-mode: bicubic;
    }

    p {
      display: block;
      margin: 13px 0;
    }
  </style>
  <!--[if mso]>
        <noscript>
        <xml>
        <o:OfficeDocumentSettings>
          <o:AllowPNG/>
          <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
        </xml>
        </noscript>
        <![endif]-->
  <!--[if lte mso 11]>
        <style type="text/css">
          .mj-outlook-group-fix { width:100% !important; }
        </style>
        <![endif]-->
  <style type="text/css">
    @media only screen and (min-width:480px) {
      .mj-column-per-80 {
        width: 80% !important;
        max-width: 80%;
      }
    }
  </style>
  <style media="screen and (min-width:480px)">
    .moz-text-html .mj-column-per-80 {
      width: 80% !important;
      max-width: 80%;
    }
  </style>
  <style type="text/css">
    @media only screen and (max-width:480px) {
      table.mj-full-width-mobile {
        width: 100% !important;
      }

      td.mj-full-width-mobile {
        width: auto !important;
      }
    }
  </style>
</head>

<body style="word-spacing:normal;background-color:#EAF0F6;">
  <div style="background-color:#EAF0F6;">
    <!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
    <div style="margin:0px auto;border-radius:20px;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;border-radius:20px;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
              <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:top;width:480px;" ><![endif]-->
              <div class="mj-column-per-80 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
                  <tbody>
                    <tr>
                      <td style="background-color:#ffffff;border-radius:20px;vertical-align:top;padding:40px;">
                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="" width="100%">
                          <tbody>
                            <tr>
                              <td align="left" style="font-size:0px;padding:0;padding-bottom:52px;word-break:break-word;">
                                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                  <tbody>
                                    <tr>
                                      <td style="width:159px;">
                                        <img height="auto" src="https://img3.airdoc.com/staticResources/H5/static/email-logo.png
" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="159" />
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </td>
                            </tr>
                            <tr>
                              <td align="left" style="font-size:0px;padding:0;padding-bottom:44px;word-break:break-word;">
                                <div style="font-family:helvetica;font-size:28px;font-weight:bold;line-height:1;text-align:left;color:#252727;">More Intelligence, Better Care</div>
                              </td>
                            </tr>
                            <tr>
                              <td align="left" style="font-size:0px;padding:0;word-break:break-word;">
                                <div style="font-family:helvetica;font-size:18px;font-weight:bold;line-height:25px;text-align:left;color:#252727;">Hi</div>
                              </td>
                            </tr>
                            <tr>
                              <td align="left" style="font-size:0px;padding:0;padding-top:20px;word-break:break-word;">
                                <div style="font-family:helvetica;font-size:18px;line-height:25px;text-align:left;color:#252727;">Hope this email can reach you well.</div>
                              </td>
                            </tr>
                            <tr>
                              <td align="left" style="font-size:0px;padding:0;padding-top:20px;word-break:break-word;">
                                <div style="font-family:helvetica;font-size:18px;line-height:25px;text-align:left;color:#252727;">Our company, Airdoc, is specialized in the fundus analysis AI (artificial intelligence), which can detect the user’s eye diseases and other systematic health risks based on the fundus image, including hypertension, diabetic, ICVD, cardiovascular disease and so on. Up to now, we can detect over 50 kinds of diseases. After you upload the fundus image into our software, the health assessment report will be generated automatically in just several minutes.</div>
                              </td>
                            </tr>
                            <tr>
                              <td align="left" style="font-size:0px;padding:0;padding-top:20px;word-break:break-word;">
                                <div style="font-family:helvetica;font-size:18px;line-height:25px;text-align:left;color:#252727;">It can be used in the optometry departments in hospitals, health check-up centers, insurance companies, optical centers and so on. So the application field is pretty wide. Many top companies around the world are using our product. We help them earn lots of incomes and helped lots of users save their eyesight or even life. Highly recommend you learn about it.</div>
                              </td>
                            </tr>
                            <tr>
                              <td align="left" style="font-size:0px;padding:0;padding-top:20px;word-break:break-word;">
                                <div style="font-family:helvetica;font-size:18px;line-height:25px;text-align:left;color:#252727;">What is more, we also have the hardware—fundus camera, which is very portable, cost-effective and intelligent.</div>
                              </td>
                            </tr>
                            <tr>
                              <td align="left" style="font-size:0px;padding:0;padding-top:20px;word-break:break-word;">
                                <div style="font-family:helvetica;font-size:18px;line-height:25px;text-align:left;color:#252727;">If you are interested, I’m always glad to provide you more information.</div>
                              </td>
                            </tr>
                            <tr>
                              <td align="left" style="font-size:0px;padding:0;padding-top:20px;word-break:break-word;">
                                <div style="font-family:helvetica;font-size:18px;line-height:25px;text-align:left;color:#252727;">Look forward to your reply and sincerely hope we can work together.</div>
                              </td>
                            </tr>
                            <tr>
                              <td align="left" style="font-size:0px;padding:0;padding-top:20px;word-break:break-word;">
                                <div style="font-family:helvetica;font-size:18px;line-height:25px;text-align:left;color:#252727;">All the best</div>
                              </td>
                            </tr>
                            <tr>
                              <td align="center" style="font-size:0px;padding:0;padding-top:50px;padding-bottom:9px;word-break:break-word;">
                                <p style="border-top:solid 4px #CE005C;font-size:1px;margin:0px auto;width:100%;">
                                </p>
                                <!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" style="border-top:solid 4px #CE005C;font-size:1px;margin:0px auto;width:400px;" role="presentation" width="400px" ><tr><td style="height:0;line-height:0;"> &nbsp;
</td></tr></table><![endif]-->
                              </td>
                            </tr>
                            <tr>
                              <td align="left" style="font-size:0px;padding:0;padding-bottom:12px;word-break:break-word;">
                                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                  <tbody>
                                    <tr>
                                      <td style="width:65px;">
                                        <img height="auto" src="https://img3.airdoc.com/staticResources/H5/static/email-logo.png
" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="65" />
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </td>
                            </tr>
                            <tr>
                              <td align="left" style="font-size:0px;padding:0;padding-top:4px;padding-bottom:2px;word-break:break-word;">
                                <div style="font-family:helvetica;font-size:13px;font-weight:bold;line-height:1;text-align:left;color:#828282;">Beijing AirdocTechnology Co. Ltd.</div>
                              </td>
                            </tr>
                            <tr>
                              <td align="left" style="font-size:0px;padding:0;padding-top:4px;word-break:break-word;">
                                <div style="font-family:helvetica;font-size:13px;font-weight:400;line-height:16px;text-align:left;color:#969696;">Address：Room 21, 4/F, Deputy Building, Building 2, No.2 A, North Xisanhuan Road, Haidian District, Beijing</div>
                              </td>
                            </tr>
                            <tr>
                              <td align="left" style="font-size:0px;padding:0;padding-top:4px;word-break:break-word;">
                                <div style="font-family:helvetica;font-size:13px;font-weight:400;line-height:1;text-align:left;color:#969696;">Zip Code：100089</div>
                              </td>
                            </tr>
                            <tr>
                              <td align="left" style="font-size:0px;padding:0;padding-top:4px;word-break:break-word;">
                                <div style="font-family:helvetica;font-size:13px;font-weight:400;line-height:13px;text-align:left;color:#969696;"><a style="color: #969696;margin-right: 5px;font-weight:400;" href="https://airdoc.com/home"><b>Home</b></a><a style="color: #969696;margin-right: 5px;font-weight:400;" href="https://airdoc.com/product?type=1"><b>Products</b></a><a style="color: #969696;margin-right: 5px;font-weight:400;" href="https://airdoc.com/contact"><b>Contect Us</b></a></div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <!--[if mso | IE]></td></tr></table><![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]></td></tr></table><![endif]-->
  </div>
</body>

</html>
"""
email = MIMEText(content, 'HTML', 'utf-8')
email['Subject'] = 'More Intelligence, Better Care'  # 定义邮件主题
email['From'] = userName_SendMail  # 发件人
email['To'] = ','.join(received_mail)  # 收件人
 
 
# 发送邮件
 
# QQ邮箱的端口号是465，其他邮箱的端口号可自行百度，非QQ邮箱，一般使用SMTP即可，不需要有SSL
smtp = smtplib.SMTP_SSL(mailserver, port=465)
smtp.login(userName_SendMail, userName_AuthCode)
smtp.sendmail(userName_SendMail, ','.join(received_mail), email.as_string())
 
smtp.quit()
print('恭喜，邮件发送成功了')


