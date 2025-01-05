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


class VultrIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vultr"

    @property
    def original_file_name(self) -> "str":
        return "vultr.svg"

    @property
    def title(self) -> "str":
        return "Vultr"

    @property
    def primary_color(self) -> "str":
        return "#007BFC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vultr</title>
     <path d="M8.36 2.172A1.194 1.194 0 007.348 1.6H1.2A1.2 1.2 0 000
 2.8a1.211 1.211 0 00.182.64l11.6 18.4a1.206 1.206 0 002.035
 0l3.075-4.874a1.229 1.229 0 00.182-.64 1.211 1.211 0
 00-.182-.642zm10.349 8.68a1.206 1.206 0 002.035 0L21.8
 9.178l2.017-3.2a1.211 1.211 0 00.183-.64 1.229 1.229 0
 00-.183-.64l-1.6-2.526a1.206 1.206 0 00-1.016-.571h-6.148a1.2 1.2 0
 00-1.201 1.2 1.143 1.143 0 00.188.64z" />
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
