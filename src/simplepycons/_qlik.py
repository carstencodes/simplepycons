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


class QlikIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qlik"

    @property
    def original_file_name(self) -> "str":
        return "qlik.svg"

    @property
    def title(self) -> "str":
        return "Qlik"

    @property
    def primary_color(self) -> "str":
        return "#009848"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Qlik</title>
     <path d="m23.7515 20.1367-3.13-2.6326c1.0862-1.7307 1.7303-3.7745
 1.7303-5.9655 0-6.1684-5.008-11.1764-11.176-11.1764S0 5.3702 0
 11.5386c0 6.168 5.008 11.176 11.1759 11.176 2.3934 0 4.6216-.7552
 6.4443-2.0438l3.3324 2.7988s.4974.4236.921-.0738l1.9884-2.3568c-.0186
 0 .3864-.4968-.1105-.9023zm-5.7078-8.598c0 3.7926-3.0747
 6.8672-6.8678 6.8672-3.7926 0-6.8678-3.0746-6.8678-6.8673 0-3.793
 3.0752-6.8678 6.8678-6.8678 3.7931 0 6.8678 3.0747 6.8678
 6.8678zm-11.287 0c0-2.4304 1.9702-4.4006 4.4006-4.4006 2.4303 0
 4.4005 1.9702 4.4005 4.4005 0 2.4304-1.9702 4.4006-4.4005
 4.4006-2.4304 0-4.4005-1.9702-4.4005-4.4006z" />
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
