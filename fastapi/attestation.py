import os
import base64
from cctrusted_base.api import CCTrustedApi
from cctrusted_vm import CCTrustedVmSdk
from starlette.responses import Response

def measure_reaponse(
    response: Response,
) -> None:
    if not os.path.exists('/sys/kernel/config/tsm/report'):
        return

    if hasattr(response, 'body'):
        data = base64.b64encode(response.body)
        cc_report = CCTrustedVmSdk.inst().get_cc_report(data=data)
        cc_type = CCTrustedApi.cc_type_str(cc_report.cc_type)
        response.headers["X-Attestation-Type"] = cc_type
        response.headers["X-Attestation-Report"] = base64.b64encode(cc_report.data).decode()

def verify_request(
) -> bool:
    # TODO
    pass
