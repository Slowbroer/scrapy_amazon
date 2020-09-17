import scrapy
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class GameWatchSpider(scrapy.Spider):
    name = 'game_watch'
    allowed_domains = ['amazon.cn']
    # start_urls = ['https://www.amazon.co.jp/-/zh/dp/B08HJ9T6GY/?coliid=IP7X31FAXDGQR&colid=389L345QS6BRA&ref_=lv_ov_lig_dp_it&th=1']
    # start_urls = ['https://www.amazon.co.jp/-/zh/dp/B08HJCVFMV/ref=bmx_2/356-4132250-5645159?_encoding=UTF8&pd_rd_i=B08HJCVFMV&pd_rd_r=adc37a60-f000-4d8c-959e-1d97bebe3fc1&pd_rd_w=Ddm6k&pd_rd_wg=wgMBB&pf_rd_p=911a6ea1-c3a8-407d-a8ac-8cf6660ea77e&pf_rd_r=AZSXKWGR19V3PTVYWQ4Q&psc=1&refRID=AZSXKWGR19V3PTVYWQ4Q']
    start_urls = ['https://www.amazon.cn/dp/B072FQV72L?ref_=Oct_DLandingS_D_5a913e9d_60&smid=A3TEGLC21NOO5Y']

    def parse(self, response):
        mail_host = "smtp.exmail.qq.com"  # 设置服务器
        mail_user = ""  # 用户名
        mail_pass = ""  # 口令
        message = MIMEText('Game&Watch', 'plain', 'utf-8')
        message['From'] = Header("Tensent Server", 'utf-8')
        message['To'] = Header("Slowbro", 'utf-8')

        subject = 'Game&Watch'
        message['Subject'] = Header(subject, 'utf-8')

        sender = 'husgie.du@tecklesol.com'
        receivers = ['mj1573975217@outlook.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        context = response.xpath('//input[@id="add-to-cart-button"]')

        if context:
            try:
                smtpObj = smtplib.SMTP_SSL()
                smtpObj.connect(mail_host, 465)  # 25 为 SMTP 端口号
                smtpObj.login(mail_user, mail_pass)
                smtpObj.sendmail(sender, receivers, message.as_string())
                print
                "邮件发送成功"
            except smtplib.SMTPException:
                print
                "Error: 无法发送邮件"
        else:
            print('failed')
