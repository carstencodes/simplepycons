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


class InteractjsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "interactjs"

    @property
    def original_file_name(self) -> "str":
        return "interactjs.svg"

    @property
    def title(self) -> "str":
        return "InteractJS"

    @property
    def primary_color(self) -> "str":
        return "#2599ED"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>InteractJS</title>
     <path d="M12.382.01C12.255.006 12.128 0 12 0A11.999 11.999 0 0 0
 1.804 18.327l9.911-17.17zm7.097 19.686L11.201 5.121 2.788
 19.689l.007.007h16.684zm.184 1.538H4.337a11.998 11.998 0 0 0 15.326
 0zm2.917-3.568A11.999 11.999 0 0 0 12.382.01l.667
 1.148zM12.383.009l-.001.001h.001V.009z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/taye/interact.js/blob/603c'''

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
