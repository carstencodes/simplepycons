#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class NorcoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "norco"

    @property
    def original_file_name(self) -> "str":
        return "norco.svg"

    @property
    def title(self) -> "str":
        return "Norco"

    @property
    def primary_color(self) -> "str":
        return "#00FF00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Norco</title>
     <path d="M11.055 2.707a.971.971 0 00-.688.387L0
 16.78h4.049l7.27-9.597 1.927 5.74 1.42-1.875-2.578-7.676a.983.983 0
 00-1.033-.666zM19.95 7.22l-7.27 9.597-1.927-5.74-1.42 1.875 2.578
 7.676a.987.987 0 001.72.28L24 7.218z" />
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