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


class TransmissionIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "transmission"

    @property
    def original_file_name(self) -> "str":
        return "transmission.svg"

    @property
    def title(self) -> "str":
        return "Transmission"

    @property
    def primary_color(self) -> "str":
        return "#D70008"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Transmission</title>
     <path d="M1.6956 9.46V22.254c0 .945.8847 1.709 1.7157
 1.709h17.1573c.878 0 1.7157-.6098
 1.7157-1.709V9.4666c-2.3323.3753-4.6177.6233-6.863.7708v5.1471h3.4315l-6.8629
 6.863-6.8628-6.863h3.4314v-5.0868c-2.339-.1207-4.6244-.3887-6.8428-.831h-.02v-.0068zM15.4214.0368v8.4177c2.2452-.1474
 4.5306-.1675 6.8629-.5428C23.2226 7.7643 24 7.1008 24
 6.0888v-3.8c0-1.012-.7841-1.6622-1.7157-1.8297-2.339-.429-4.6177-.2949-6.863-.4222zM8.5585.0503C6.2396.191
 3.9609.077 1.7157.459.7774.6199 0 1.2767 0 2.2887v3.8001c0 1.012.7841
 1.642 1.7157 1.823 2.2184.4423 4.5038.4758 6.8428.6031V.0503z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/transmission/transmission/
blob/7c9e04d035f3f75a8124e83d612701824487eb4e/gtk/icons/hicolor_apps_s'''

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
