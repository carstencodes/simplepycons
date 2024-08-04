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


class TeamviewerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "teamviewer"

    @property
    def original_file_name(self) -> "str":
        return "teamviewer.svg"

    @property
    def title(self) -> "str":
        return "TeamViewer"

    @property
    def primary_color(self) -> "str":
        return "#004680"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TeamViewer</title>
     <path d="M22.597 24H1.406A1.41 1.41 0 0 1 0 22.594V1.406A1.41
 1.41 0 0 1 1.406 0h21.191a1.41 1.41 0 0 1 1.406 1.406v21.188A1.41
 1.41 0 0 1 22.597 24zM11.911 2.109c-5.405.047-9.763 4.482-9.802
 9.89-.04 5.507 4.381 9.885 9.89 9.89 5.415.003 9.796-4.5
 9.89-9.89.097-5.572-4.406-9.939-9.978-9.89zM9.65 8.633l-.889
 2.159H15.3l-.889-2.159 6.642 3.365-6.642 3.365.889-2.159H8.761l.882
 2.159-6.659-3.365z" />
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
