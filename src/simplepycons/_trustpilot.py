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


class TrustpilotIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "trustpilot"

    @property
    def original_file_name(self) -> "str":
        return "trustpilot.svg"

    @property
    def title(self) -> "str":
        return "Trustpilot"

    @property
    def primary_color(self) -> "str":
        return "#00B67A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Trustpilot</title>
     <path d="M17.227 16.67l2.19 6.742-7.413-5.388 5.223-1.354zM24
 9.31h-9.165L12.005.589l-2.84 8.723L0 9.3l7.422 5.397-2.84 8.714
 7.422-5.388 4.583-3.326L24 9.311z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://support.trustpilot.com/hc/en-us/artic'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://support.trustpilot.com/hc/en-us/artic'''

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
