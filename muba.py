text = '''<xml>
                <ToUserName>![CDATA[%s]]</ToUserName>
                <FromUserName>![CDATA[%s]]</FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType>![CDATA[text]]</MsgType>
                <Content>![CDATA[%s]]</Content>
                </xml>'''


def remuba():
	return text
