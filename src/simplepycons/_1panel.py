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


class OnePanelIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "1panel"

    @property
    def original_file_name(self) -> "str":
        return "1panel.svg"

    @property
    def title(self) -> "str":
        return "1Panel"

    @property
    def primary_color(self) -> "str":
        return "#0854C1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>1Panel</title>
     <path d="m12 0 10.349 6v12L12 24 1.651 18V6zm0 .326L1.897
 6.158v11.664L12 23.653l10.103-5.831V6.158zM8.84
 20.523l-5.801-3.349V6.826L12 1.653l2.23 1.287-8.925 5.195v7.73l5.792
 3.345zm6.299-17.058 5.822 3.361v10.348L12 22.347l-2.274-1.312
 8.969-5.17v-7.73l-5.823-3.362zm-2.137 3.35v2.869l.024
 7.666-.691.384-2.18-1.249.008-6.801H8.958L8.95 8.351l3.412-1.965z" />
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
