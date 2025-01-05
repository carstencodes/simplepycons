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


class IciciBankIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "icicibank"

    @property
    def original_file_name(self) -> "str":
        return "icicibank.svg"

    @property
    def title(self) -> "str":
        return "ICICI Bank"

    @property
    def primary_color(self) -> "str":
        return "#AE282E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ICICI Bank</title>
     <path d="M21.9258 2.0961C19.279-1.6476 12.698-.2426 7.2138
 5.2416c-5.484 5.475-7.7865 12.9625-5.1397 16.7062.8728 1.2386 2.1837
 1.902 3.7386 2.0522 1.0516.0078 1.9129-1.1846
 2.6158-2.7774.7252-1.6678 1.1694-3.218
 1.5138-4.6592.5077-2.2934.544-3.934.29-4.2786-.435-.5801-1.4321-.435-2.5561.2176-.544.2991-1.26.0997-.408-.9336.8612-1.0425
 4.2605-3.5625 5.4933-3.9523 1.3415-.3898 2.8734.136 2.3568
 1.6226-.3706 1.0847-5.0473 13.486-1.596 12.2719 1.1049-.747
 2.205-1.6497 3.2639-2.7086 5.4841-5.475 7.7865-12.9625
 5.1396-16.7063zm-5.3662 3.209c-1.0969 1.0968-2.52
 1.4865-3.1364.852-.6617-.6345-.272-2.0577.8249-3.1726 1.1058-1.115
 2.529-1.4594 3.1454-.834.6345.6436.2448 2.0487-.834 3.1545z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.icicibank.com/ms/aboutus/annual-r'''

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
