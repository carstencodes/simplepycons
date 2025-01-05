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


class QualysIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qualys"

    @property
    def original_file_name(self) -> "str":
        return "qualys.svg"

    @property
    def title(self) -> "str":
        return "Qualys"

    @property
    def primary_color(self) -> "str":
        return "#ED2E26"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Qualys</title>
     <path d="M11.9986 0C5.4353 0 2.1382 3.5117 2.1382 3.5117s-.3775
 2.5993-.1366 7.8332C2.3654 19.2513 11.999 24.0005 11.9999
 24c.001-.0005 9.6347-4.7488
 9.9985-12.6551.2408-5.2339-.1364-7.8332-.1364-7.8332S18.562 0 11.9986
 0zm-.6782 2.9194a7.3657 7.3657 0 0 1 8.0454 7.3343 7.1158 7.1158 0 0
 1-2.7712 5.6342c-1.1788-.108-2.4098-.4423-2.9676-.7605 1.4379-.9177
 3.3036-2.7033 3.3036-4.8737a4.9361 4.9361 0 0 0-4.9305-4.9305c-2.7165
 0-4.9266 2.2743-4.9266 5.0698 0 2.332 1.2355 4.1624 3.6718 5.4404
 1.5943.8363 3.9724 1.449 6.4852 1.7723-.418.6225-1.533 1.686-2.1847
 2.0462-3.0087-.4934-5.6513-1.5354-7.4578-3.0964-1.9323-1.6699-2.9536-3.8488-2.9536-6.3018a7.3657
 7.3657 0 0 1 6.686-7.3343Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.qualys.com/company/newsroom/media'''
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
