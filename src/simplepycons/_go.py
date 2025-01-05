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


class GoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "go"

    @property
    def original_file_name(self) -> "str":
        return "go.svg"

    @property
    def title(self) -> "str":
        return "Go"

    @property
    def primary_color(self) -> "str":
        return "#00ADD8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Go</title>
     <path d="M1.811 10.231c-.047
 0-.058-.023-.035-.059l.246-.315c.023-.035.081-.058.128-.058h4.172c.046
 0 .058.035.035.07l-.199.303c-.023.036-.082.07-.117.07zM.047
 11.306c-.047
 0-.059-.023-.035-.058l.245-.316c.023-.035.082-.058.129-.058h5.328c.047
 0 .07.035.058.07l-.093.28c-.012.047-.058.07-.105.07zm2.828
 1.075c-.047
 0-.059-.035-.035-.07l.163-.292c.023-.035.07-.07.117-.07h2.337c.047 0
 .07.035.07.082l-.023.28c0
 .047-.047.082-.082.082zm12.129-2.36c-.736.187-1.239.327-1.963.514-.176.046-.187.058-.34-.117-.174-.199-.303-.327-.548-.444-.737-.362-1.45-.257-2.115.175-.795.514-1.204
 1.274-1.192 2.22.011.935.654 1.706 1.577 1.835.795.105 1.46-.175
 1.987-.77.105-.13.198-.27.315-.434H10.47c-.245
 0-.304-.152-.222-.35.152-.362.432-.97.596-1.274a.315.315 0
 01.292-.187h4.253c-.023.316-.023.631-.07.947a4.983 4.983 0 01-.958
 2.29c-.841 1.11-1.94 1.8-3.33
 1.986-1.145.152-2.209-.07-3.143-.77-.865-.655-1.356-1.52-1.484-2.595-.152-1.274.222-2.419.993-3.424.83-1.086
 1.928-1.776 3.272-2.02 1.098-.2 2.15-.07 3.096.571.62.41 1.063.97
 1.356 1.648.07.105.023.164-.117.2m3.868
 6.461c-1.064-.024-2.034-.328-2.852-1.029a3.665 3.665 0
 01-1.262-2.255c-.21-1.32.152-2.489.947-3.529.853-1.122 1.881-1.706
 3.272-1.95 1.192-.21 2.314-.095 3.33.595.923.63 1.496 1.484 1.648
 2.605.198 1.578-.257 2.863-1.344 3.962-.771.783-1.718 1.273-2.805
 1.495-.315.06-.63.07-.934.106zm2.78-4.72c-.011-.153-.011-.27-.034-.387-.21-1.157-1.274-1.81-2.384-1.554-1.087.245-1.788.935-2.045
 2.033-.21.912.234 1.835 1.075 2.21.643.28 1.285.244 1.905-.07.923-.48
 1.425-1.228 1.484-2.233z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
