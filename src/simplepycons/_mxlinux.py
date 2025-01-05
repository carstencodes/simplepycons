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


class MxLinuxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mxlinux"

    @property
    def original_file_name(self) -> "str":
        return "mxlinux.svg"

    @property
    def title(self) -> "str":
        return "MX Linux"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MX Linux</title>
     <path d="M12.001 13.301l3.277
 3.819-.75.9-2.133-2.521-1.131-1.338.737-.86zM24 2.41v19.182c0
 .655-.531 1.186-1.186 1.186H1.186A1.186 1.186 0 0 1 0
 21.591V2.409c0-.655.531-1.186 1.186-1.186h21.628c.655 0 1.186.53
 1.186 1.186zm-2.241
 17.09l-2.116-2.542-2.115-2.541-.586.704-3.25-3.788
 4.913-5.73-1.175-1.008-4.76 5.549-4.743-5.527-1.947 1.67 5
 5.827-.73.851-1.24-1.465-3.384 4-3.385 4h19.518z" />
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
