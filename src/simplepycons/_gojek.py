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


class GojekIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gojek"

    @property
    def original_file_name(self) -> "str":
        return "gojek.svg"

    @property
    def title(self) -> "str":
        return "Gojek"

    @property
    def primary_color(self) -> "str":
        return "#00AA13"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gojek</title>
     <path d="M12.072.713a15.38 15.38 0 0 0-.643.011C5.317.998.344
 5.835.017 11.818c-.266 4.913 2.548 9.21 6.723 11.204 1.557.744
 3.405-.19
 3.706-1.861.203-1.126-.382-2.241-1.429-2.742-2.373-1.139-3.966-3.602-3.778-6.406.22-3.28
 2.931-5.945 6.279-6.171 3.959-.267 7.257 2.797 7.257 6.619 0
 2.623-1.553 4.888-3.809 5.965a2.511 2.511 0 0 0-1.395
 2.706l.011.056c.295 1.644 2.111 2.578 3.643 1.852C21.233 21.139 24
 17.117 24 12.461 23.996 5.995 18.664.749 12.072.711v.002Zm-.061
 7.614c-2.331 0-4.225 1.856-4.225 4.139 0 2.282 1.894 4.137 4.225
 4.137 2.33 0 4.225-1.855 4.225-4.137
 0-2.283-1.895-4.139-4.225-4.139Z" />
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
