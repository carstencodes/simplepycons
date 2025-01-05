#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class RichIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rich"

    @property
    def original_file_name(self) -> "str":
        return "rich.svg"

    @property
    def title(self) -> "str":
        return "Rich"

    @property
    def primary_color(self) -> "str":
        return "#FAE742"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rich</title>
     <path d="M9.419 10.32v-.645c0-.531.437-.968.968-.968h3.225c.204 0
 .395.065.552.175a2.295 2.295 0 0 0-.904.47h-2.873c-.177
 0-.323.146-.323.323v3.224c0
 .177.146.323.323.323h2.921l.048.067v.578h-2.969c-.531
 0-.968-.437-.968-.968v-1.934h-5.13l.08.967h3.115v.645H4.423l.058.698c.651.192
 1.323.309 2.001.347.901.038 1.789.229
 2.625.564.138.04.244.146.288.276a4.183 4.183 0 0
 0-1.771-.395H6.88c-.25 0-.485.065-.688.18a9.4449 9.4449 0 0
 1-1.654-.286l.147
 1.772c.267-.044.533-.095.798-.15.018.224.09.434.203.616-.314.067-.63.127-.947.179l.09
 1.09c.03.332.31.589.643.591h2.101c-.335.14-.626.364-.846.645H5.472c-.666-.003-1.226-.519-1.285-1.183l-.548-6.556H2.358l.758
 7.578c.081.821.78 1.453 1.605
 1.451h1.565c.001.121.012.239.033.355-.293.04-.566.141-.806.29h-.792c-1.155.004-2.134-.882-2.246-2.032l-.794-7.933c-.001-.01-.001-.021-.001-.032
 0-.088.036-.169.094-.228l2.58-2.58a.324.324 0 0 1
 .228-.094h1.023a.9628.9628 0 0
 1-.056-.323c0-.435.294-.819.713-.933a.9928.9928 0 0
 1-.068-.357c0-.53.437-.967.968-.967h1.29c.531 0 .967.437.967.967 0
 .099-.015.198-.045.293a.976.976 0 0 1 .436-.258.9719.9719 0 0
 1-.068-.357c0-.531.437-.968.967-.968h1.29c.531 0 .968.437.968.968 0
 .11-.019.219-.055.322h1.667c.331 0 .639.17.816.449a.9527.9527 0 0 1
 .474-.126h2.58c.531 0 .968.436.968.967 0
 .11-.019.219-.056.323h.461l-.282-.174
 1.876-3.051h-2.645V3.87h.637a5.077 5.077 0 0
 0-.027-.323c-.64-.002-.853-.011-1.57-.04l-.09-.004a2.6858 2.6858 0 0
 1-.673-.089.4482.4482 0 0 1-.267-.189.4067.4067 0 0
 1-.041-.282.455.455 0 0 1
 .238-.274c.059-.032.12-.062.181-.089h-3.87v1.29h4.837v.645H2.579l1.087
 1.766-.549.338-1.389-2.258a.3145.3145 0 0 1-.048-.169C1.68 1.802
 3.205 0 5.227 0h.078c.403 0
 .747.275.855.645h11.679c.107-.37.451-.645.854-.645h.078c2.023 0 3.548
 1.802 3.548 4.192a.318.318 0 0 1-.067.196L20.191 7.74h.193c.53 0
 .967.437.967.967 0 .224-.078.441-.22.614l1.083
 1.082c.065.06.106.145.106.239 0 .011 0 .022-.001.032l-.794 7.933c-.11
 1.131-1.059 2.006-2.188 2.032a2.053 2.053 0 0
 0-.805-.29c.021-.116.032-.234.032-.355h.714c.824.002 1.524-.63
 1.604-1.451l.76-7.578h-1.283l-.546 6.556c-.059.664-.62 1.18-1.287
 1.183h-.403c-.094-.12-.201-.23-.319-.328v-.317h.722c.333-.002.613-.259.643-.591l.004-.054c-.578
 0-1.099-.002-1.636-.018v-.645c.553.017 1.091.018
 1.69.018l.08-.96c-.666.022-1.243.098-1.77.237v-.665c.549-.13
 1.145-.201
 1.824-.219l.081-.971c-.637.008-1.272.043-1.905.105v-.647a23.275
 23.275 0 0 1
 1.958-.103l.081-.969h-1.521c.134-.2.234-.417.298-.645h1.276l.081-.967h-1.276a2.2538
 2.2538 0 0 0-.129-.645h2.079c.177 0 .322-.146.322-.323a.323.323 0 0
 0-.322-.322.3248.3248 0 0 1-.323-.323c0-.177.146-.322.323-.322.177 0
 .322-.146.322-.323a.323.323 0 0 0-.322-.322h-1.935a.3248.3248 0 0
 1-.323-.323c0-.177.146-.322.323-.322.177 0
 .322-.146.322-.323a.323.323 0 0 0-.322-.322h-2.58a.321.321 0 0
 0-.277.161c-.057.1-.164.161-.279.161h-.089a.323.323 0 0
 1-.322-.322c0-.177-.146-.323-.323-.323h-2.58a.323.323 0 0
 1-.322-.322c0-.177.145-.323.322-.323.177 0 .323-.145.323-.322
 0-.177-.146-.323-.323-.323h-1.29c-.177 0-.322.146-.322.323 0
 .177.145.322.322.322.177 0 .323.146.323.323 0
 .177-.146.322-.323.322h-.645a.323.323 0 0 0-.302.218.3227.3227 0 0
 1-.305.215.327.327 0 0 1-.179-.054.3172.3172 0 0
 0-.181-.056h-.645a.3248.3248 0 0
 1-.323-.323c0-.177.146-.322.323-.322.177 0
 .322-.146.322-.323a.323.323 0 0 0-.322-.322h-1.29c-.177
 0-.323.145-.323.322 0 .177.146.323.323.323.177 0 .322.145.322.322 0
 .177-.145.323-.322.323h-.645c-.177 0-.323.145-.323.322 0
 .177.146.323.323.323.177 0 .322.145.322.322 0
 .177-.145.323-.322.323H4.904c-.176 0-.322.145-.322.322 0
 .177.146.323.322.323.177 0 .323.145.323.322 0
 .177-.146.323-.323.323H4.26c-.177 0-.323.145-.323.322 0
 .177.146.323.323.323h1.289a.3117.3117 0 0 0 .081-.013.3177.3177 0 0 1
 .162 0c.026.007.053.012.08.013h2.58c.177 0
 .322-.146.322-.323a.323.323 0 0 0-.322-.322h-.968V9.03h.968c.531 0
 .967.436.967.967 0
 .113-.019.222-.056.323h.056Zm3.225-6.45V1.29h-1.29v2.58h1.29Zm-10.309
 0h1.609c.089-1.854.936-2.52 1.452-2.754A.2513.2513 0 0 0
 5.55.89c0-.134-.11-.245-.244-.245h-.079C3.662.645 2.46 2.01 2.335
 3.87Zm2.255 0h6.119V2.257c-1.154
 0-2.459.001-3.508.003h-.077c.065.041.136.079.208.119.127.066.25.141.368.223a.43.43
 0 0 1 .18.536.4527.4527 0 0
 1-.258.228c-.223.079-.458.121-.696.123-.793.043-1.475.055-2.309.058-.012.102-.021.21-.027.323Zm14.663-.969c-.226-.759-.637-1.071-.917-1.198a.903.903
 0 0 1-.434-.413h-4.613v.645c1.274 0 3.003 0
 4.155.002h.055c.129-.006.259.004.385.032.259.037.451.267.44.528a.5407.5407
 0 0 1-.265.373c.494.021.727.029 1.194.031ZM6.096 1.29a.8943.8943 0 0
 1-.434.413c-.279.127-.691.439-.917 1.198.751-.003 1.383-.016
 2.103-.054-.104-.06-.203-.129-.295-.207a.6246.6246 0 0
 1-.235-.405c-.008-.263.164-.5.417-.572.132-.04.271-.056.409-.048h.055c1.051-.002
 2.356-.003 3.51-.003V1.29H6.096Zm-3.315 9.03h.566a.9616.9616 0 0
 1-.056-.323c0-.072.008-.143.024-.212l-.534.535Zm17.273-6.45h1.609C21.538
 2.01 20.337.645 18.771.645h-.078a.245.245 0 0
 0-.244.244c.002.099.063.188.154.226.516.235 1.362.901 1.451
 2.755Zm-6.698
 12.638c-.345.098-.701.162-1.062.19-.197.025-.395.047-.593.069-.056.004-.111.008-.167.014a3.995
 3.995 0 0
 0-.289-.618c.129-.015.257-.027.386-.037.193-.022.387-.043.58-.068.391-.027.776-.102
 1.145-.222v.672Zm-.284-3.609h-2.363a.323.323 0 0
 1-.322-.322v-2.58c0-.177.145-.322.322-.322h2.24c-.153.192-.275.409-.359.645h-1.558v1.934h1.627c.064.141.143.276.236.403l.177.242Zm-5.467
 5.147.005-.01v.008l-.005.002ZM3.292 11.61v.644h-.645v-.644h.645Zm1.29
 7.094v.645h-.645v-.645h.645Zm16.769-7.417v.645h-.645v-.645h.645Zm-1.29
 7.417v.645h-.645v-.645h.645ZM8.774
 11.932v.645h-.645v-.645h.645Zm3.548-1.29v1.29h-.645v-1.29h.645ZM4.064
 6.927l.395.642-.549.338-.395-.642.549-.338Zm14.18 13.902c.875 0
 1.586.712 1.586 1.585 0 .875-.711 1.586-1.586 1.586H6.606c-.875
 0-1.585-.711-1.585-1.586 0-.873.71-1.585
 1.585-1.585h.427c-.155-.246-.247-.534-.247-.845 0-.785.574-1.437
 1.324-1.563v-.786c0-.385-.172-.744-.473-.986l-.034-.028a1.158 1.158 0
 0 0-.723-.254c-.497 0-.902-.404-.902-.9s.405-.9.902-.9h.744c.836 0
 1.653.288 2.304.812.866.697 1.363 1.733 1.363
 2.842v.177h2.565v-5.272l-.557-.764c-.223-.306-.342-.666-.342-1.045v-.233c0-.979.799-1.775
 1.781-1.775h1.418c.982 0 1.781.796 1.781 1.775v.233c0
 .379-.118.739-.341 1.045l-.559.764v5.376c.599.226 1.027.805 1.027
 1.482 0 .311-.092.599-.246.845h.426Zm-3.385-5.232a.263.263 0 0
 1-.021-.372l.345-.389v-.794a1.7787 1.7787 0 0
 1-.586-.196v4.552h1.7v-4.552c-.181.099-.379.165-.585.196v.794l.345.389a.264.264
 0 0 1-.023.372.2624.2624 0 0 1-.175.068.2668.2668 0 0
 1-.198-.089l-.214-.241-.214.241a.2668.2668 0 0 1-.198.089.2649.2649 0
 0 1-.176-.068Zm-6.758.475c.476.384.75.953.75
 1.563v.763h1.7v-.177a2.98 2.98 0 0
 0-.076-.662l-.406-.062c-.733-.114-1.307-.704-1.398-1.438l-.072-.585a2.9598
 2.9598 0 0 0-.975-.167H6.88c-.089 0-.162.072-.162.16 0
 .088.073.159.162.159.431 0 .852.149 1.186.418l.035.028Zm8.342
 7.188c.402-.819 1.152-1.415 2.057-1.616l.06-.012a.8101.8101 0 0
 0-.316-.063H6.606c-.466 0-.845.38-.845.845 0
 .467.379.846.845.846h.558l-.007-.006a.8244.8244 0 0
 1-.265-.604c0-.409.307-.76.714-.816l.985-.136c.343-.047.696.071.942.315.309.309.41.773.255
 1.182l-.025.065h6.68Zm-8.817-3.672a.836.836 0 0 0-.099.396c0
 .466.379.845.846.845h4.31c.082-.551.464-1.022
 1.001-1.211.419-.147.881-.106
 1.266.114l.199.113c.374.214.636.574.73.984h.599c.466 0
 .846-.379.846-.845
 0-.467-.38-.846-.846-.846h-4.935l-.125.202c-.405.654-1.108
 1.017-1.831 1.017-.348
 0-.701-.085-1.028-.261l-.933-.508Zm6.072-8.271c0
 .22.068.431.199.608l.709.971c.195.267.509.427.841.427.331 0
 .646-.16.841-.427l.71-.971c.13-.177.199-.388.199-.608v-.233c0-.451-.293-.835-.698-.976v.301c0
 .146-.119.265-.265.265a.2646.2646 0 0 1-.264-.265v-.359h-.258v.684c0
 .146-.119.265-.265.265a.2646.2646 0 0 1-.264-.265v-.684h-.258v.359c0
 .146-.119.265-.265.265a.2646.2646 0 0
 1-.264-.265v-.301c-.406.141-.698.525-.698.976v.233Zm1.157.309c0
 .166-.135.301-.303.301a.3015.3015 0 0 1-.302-.301.3026.3026 0 0 1
 .605 0Zm1.672.012c0 .166-.136.302-.303.302a.3024.3024 0 0
 1-.302-.302c0-.166.135-.301.302-.301.167 0 .303.135.303.301Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Textualize/rich/blob/fd981'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
