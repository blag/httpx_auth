import time_machine
from pytest_httpx import HTTPXMock
import httpx

import httpx_auth


@time_machine.travel("2018-10-11T15:05:05.663979+00:00", tick=False)
def test_aws_auth_without_content_in_request(httpx_mock: HTTPXMock):
    auth = httpx_auth.AWS4Auth(
        access_id="access_id",
        secret_key="wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY",
        region="us-east-1",
        service="iam",
    )

    httpx_mock.add_response(
        url="https://authorized_only",
        method="POST",
        match_headers={
            "x-amz-content-sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "Authorization": "AWS4-HMAC-SHA256 Credential=access_id/20181011/us-east-1/iam/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=ce708380ee69b1a9558b9b0dddd4d15f35a2a5e5ea3534b541247f1a746626db",
            "x-amz-date": "20181011T150505Z",
        },
    )
    with httpx.Client() as client:
        client.post("https://authorized_only", auth=auth)


@time_machine.travel("2018-10-11T15:05:05.663979+00:00", tick=False)
def test_aws_auth_with_content_in_request(httpx_mock: HTTPXMock):
    auth = httpx_auth.AWS4Auth(
        access_id="access_id",
        secret_key="wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY",
        region="us-east-1",
        service="iam",
    )

    httpx_mock.add_response(
        url="https://authorized_only",
        method="POST",
        match_json=[{"key": "value"}],
        match_headers={
            "x-amz-content-sha256": "fb65c1441d6743274738fe3b3042a73167ba1fb2d34679d8dd16433473758f97",
            "Authorization": "AWS4-HMAC-SHA256 Credential=access_id/20181011/us-east-1/iam/aws4_request, SignedHeaders=content-type;host;x-amz-content-sha256;x-amz-date, Signature=5f4f832a19fc834d4f34047289ad67d96da25bd414a70f02ce6b85aef9ab8068",
            "x-amz-date": "20181011T150505Z",
        },
    )
    with httpx.Client() as client:
        client.post("https://authorized_only", json=[{"key": "value"}], auth=auth)


@time_machine.travel("2018-10-11T15:05:05.663979+00:00", tick=False)
def test_aws_auth_with_security_token_and_without_content_in_request(
    httpx_mock: HTTPXMock,
):
    auth = httpx_auth.AWS4Auth(
        access_id="access_id",
        secret_key="wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY",
        region="us-east-1",
        service="iam",
        security_token="security_token",
    )

    httpx_mock.add_response(
        url="https://authorized_only",
        method="POST",
        match_headers={
            "x-amz-content-sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "Authorization": "AWS4-HMAC-SHA256 Credential=access_id/20181011/us-east-1/iam/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date;x-amz-security-token, Signature=2ae27ce5e8dcc005736c97ff857e4f44401fc3a33d8358b1d67c079f0f5a8b3e",
            "x-amz-date": "20181011T150505Z",
            "x-amz-security-token": "security_token",
        },
    )
    with httpx.Client() as client:
        client.post("https://authorized_only", auth=auth)


@time_machine.travel("2018-10-11T15:05:05.663979+00:00", tick=False)
def test_aws_auth_with_security_token_and_content_in_request(httpx_mock: HTTPXMock):
    auth = httpx_auth.AWS4Auth(
        access_id="access_id",
        secret_key="wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY",
        region="us-east-1",
        service="iam",
        security_token="security_token",
    )

    httpx_mock.add_response(
        url="https://authorized_only",
        method="POST",
        match_json=[{"key": "value"}],
        match_headers={
            "x-amz-content-sha256": "fb65c1441d6743274738fe3b3042a73167ba1fb2d34679d8dd16433473758f97",
            "Authorization": "AWS4-HMAC-SHA256 Credential=access_id/20181011/us-east-1/iam/aws4_request, SignedHeaders=content-type;host;x-amz-content-sha256;x-amz-date;x-amz-security-token, Signature=e02c4733589cf6e80361f6905564da6d0c23a0829bb3c3899b328e43b2f7b581",
            "x-amz-date": "20181011T150505Z",
            "x-amz-security-token": "security_token",
        },
    )
    with httpx.Client() as client:
        client.post("https://authorized_only", json=[{"key": "value"}], auth=auth)


@time_machine.travel("2018-10-11T15:05:05.663979+00:00", tick=False)
def test_aws_auth_override_x_amz_date_header(httpx_mock: HTTPXMock):
    auth = httpx_auth.AWS4Auth(
        access_id="access_id",
        secret_key="wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY",
        region="us-east-1",
        service="iam",
    )

    httpx_mock.add_response(
        url="https://authorized_only",
        method="POST",
        match_headers={
            "x-amz-content-sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "Authorization": "AWS4-HMAC-SHA256 Credential=access_id/20181011/us-east-1/iam/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=ce708380ee69b1a9558b9b0dddd4d15f35a2a5e5ea3534b541247f1a746626db",
            "x-amz-date": "20181011T150505Z",
        },
    )
    with httpx.Client() as client:
        client.post(
            "https://authorized_only",
            headers={"x-amz-date": "20201011T150505Z"},
            auth=auth,
        )


@time_machine.travel("2018-10-11T15:05:05.663979+00:00", tick=False)
def test_aws_auth_root_path(httpx_mock: HTTPXMock):
    auth = httpx_auth.AWS4Auth(
        access_id="access_id",
        secret_key="wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY",
        region="us-east-1",
        service="iam",
    )

    httpx_mock.add_response(
        url="https://authorized_only/",
        method="POST",
        match_headers={
            "x-amz-content-sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "Authorization": "AWS4-HMAC-SHA256 Credential=access_id/20181011/us-east-1/iam/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=ce708380ee69b1a9558b9b0dddd4d15f35a2a5e5ea3534b541247f1a746626db",
            "x-amz-date": "20181011T150505Z",
        },
    )
    with httpx.Client() as client:
        client.post("https://authorized_only/", auth=auth)


@time_machine.travel("2018-10-11T15:05:05.663979+00:00", tick=False)
def test_aws_auth_query_parameters(httpx_mock: HTTPXMock):
    auth = httpx_auth.AWS4Auth(
        access_id="access_id",
        secret_key="wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY",
        region="us-east-1",
        service="iam",
    )

    httpx_mock.add_response(
        url="https://authorized_only?param1&param2=blah*",
        method="POST",
        match_headers={
            "x-amz-content-sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "Authorization": "AWS4-HMAC-SHA256 Credential=access_id/20181011/us-east-1/iam/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=f2b8a73e388dc04586b5bcc208c6e50d92f04a1296e561229cd88811ad2494e9",
            "x-amz-date": "20181011T150505Z",
        },
    )
    with httpx.Client() as client:
        client.post("https://authorized_only?param1&param2=blah*", auth=auth)


@time_machine.travel("2018-10-11T15:05:05.663979+00:00", tick=False)
def test_aws_auth_path_normalize(httpx_mock: HTTPXMock):
    auth = httpx_auth.AWS4Auth(
        access_id="access_id",
        secret_key="wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY",
        region="us-east-1",
        service="iam",
    )

    httpx_mock.add_response(
        url="https://authorized_only/stuff//more/",
        method="POST",
        match_headers={
            "x-amz-content-sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "Authorization": "AWS4-HMAC-SHA256 Credential=access_id/20181011/us-east-1/iam/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=e49fb885d30c9e74901071748b783fabe8ba7a979aa20420ac76af1dda1edd03",
            "x-amz-date": "20181011T150505Z",
        },
    )
    with httpx.Client() as client:
        client.post("https://authorized_only/./test/../stuff//more/", auth=auth)


@time_machine.travel("2018-10-11T15:05:05.663979+00:00", tick=False)
def test_aws_auth_path_quoting(httpx_mock: HTTPXMock):
    auth = httpx_auth.AWS4Auth(
        access_id="access_id",
        secret_key="wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY",
        region="us-east-1",
        service="iam",
    )

    httpx_mock.add_response(
        url="https://authorized_only/test/hello-*.&%5E~+%7B%7D!$%C2%A3_%20",
        method="POST",
        match_headers={
            "x-amz-content-sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "Authorization": "AWS4-HMAC-SHA256 Credential=access_id/20181011/us-east-1/iam/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=f3c8efd9b81b952035a73ea93d3a79380e13370bcaa6089e4275319bde17a400",
            "x-amz-date": "20181011T150505Z",
        },
    )
    with httpx.Client() as client:
        client.post("https://authorized_only/test/hello-*.&^~+{}!$£_ ", auth=auth)


@time_machine.travel("2018-10-11T15:05:05.663979+00:00", tick=False)
def test_aws_auth_path_percent_encode_non_s3(httpx_mock: HTTPXMock):
    auth = httpx_auth.AWS4Auth(
        access_id="access_id",
        secret_key="wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY",
        region="us-east-1",
        service="iam",
    )

    httpx_mock.add_response(
        url="https://authorized_only/test/%2a%2b%25/~-_%5E&%20%25%25",
        method="POST",
        match_headers={
            "x-amz-content-sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "Authorization": "AWS4-HMAC-SHA256 Credential=access_id/20181011/us-east-1/iam/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=7b3267f1b4bcb1f6731eb99aa9b3381225c18fc32e3ecb78fc4adceb746f92f3",
            "x-amz-date": "20181011T150505Z",
        },
    )
    with httpx.Client() as client:
        client.post("https://authorized_only/test/%2a%2b%25/~-_^& %%", auth=auth)


@time_machine.travel("2018-10-11T15:05:05.663979+00:00", tick=False)
def test_aws_auth_path_percent_encode_s3(httpx_mock: HTTPXMock):
    auth = httpx_auth.AWS4Auth(
        access_id="access_id",
        secret_key="wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY",
        region="us-east-1",
        service="s3",
    )

    httpx_mock.add_response(
        url="https://authorized_only/test/%2a%2b%25/~-_%5E&%20%25%25",
        method="POST",
        match_headers={
            "x-amz-content-sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "Authorization": "AWS4-HMAC-SHA256 Credential=access_id/20181011/us-east-1/s3/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=dd3e44f87a05d1488fa5aca66702e8c53a0d0fa570564bc70941bc5c6d25016d",
            "x-amz-date": "20181011T150505Z",
        },
    )
    with httpx.Client() as client:
        client.post("https://authorized_only/test/%2a%2b%25/~-_^& %%", auth=auth)


@time_machine.travel("2018-10-11T15:05:05.663979+00:00", tick=False)
def test_aws_auth_without_path(httpx_mock: HTTPXMock):
    auth = httpx_auth.AWS4Auth(
        access_id="access_id",
        secret_key="wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY",
        region="us-east-1",
        service="iam",
    )

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "x-amz-content-sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "Authorization": "AWS4-HMAC-SHA256 Credential=access_id/20181011/us-east-1/iam/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=e3411118ac098a820690144b8b273aa64a3366d899fa68fd64a1ab950c982b4b",
            "x-amz-date": "20181011T150505Z",
        },
    )
    with httpx.Client() as client:
        client.get("https://authorized_only", auth=auth)
