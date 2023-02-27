from app.src.log.log_configuration import log


def set_html_template_email(payloademail):
    logger = log()

    logger.info("Iniciando formatação do html para envio do e-mail")
    logger.info(f"Payload com dados para envio do e-mail: {payloademail}")

    emails_body = []

    for email in payloademail:
        logger.info("Formatando email por email")
        logger.info(f"Email parameters recebido. {email}")

        html_email_content = {
            "subject": f"KDRAMA {email['name']} YOU REALLY SHOULD WATCH",
            "emailbody": f"""
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>KOREAN SERIE TV TO WATCH</title>
                </head>
                <h1 style='text-align:center'>List of K-DRAMAS</h1>
                <img src="mvedramacapa.jpg" alt="mvedramacapa" width="250" height="250">
                
                <p>Hey, how are you? Today i'm going yo recomend to you 3 south korean dramas,
                that you can watch in your free time! So he we go!
                </p>
                
                  <div>
                    <p>
                        k-drama: {email['name']} <br>
                        Release date: {email['release']} <br>
                        Genra: {email['genra']} <br>
                        Director: {email['director']}   <br>
                  
                  
                  </div>
                </body>
            </html>
        """
        }
        emails_body.append(html_email_content)

    if emails_body is None:
        logger.error("Não foi possivel formatar e-mails.")
    else:
        logger.info("Formatação finalizada com sucesso")
        logger.info(f"E-mails formatados. {emails_body}")

    return emails_body



