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


class PrettierIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "prettier"

    @property
    def original_file_name(self) -> "str":
        return "prettier.svg"

    @property
    def title(self) -> "str":
        return "Prettier"

    @property
    def primary_color(self) -> "str":
        return "#F7B93E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Prettier</title>
     <path d="M8.571 23.429A.571.571 0 0 1 8 24H2.286a.571.571 0 0 1
 0-1.143H8c.316 0 .571.256.571.572zM8 20.57H6.857a.571.571 0 0 0 0
 1.143H8a.571.571 0 0 0 0-1.143zm-5.714 1.143H4.57a.571.571 0 0 0
 0-1.143H2.286a.571.571 0 0 0 0 1.143zM8 18.286H2.286a.571.571 0 0 0 0
 1.143H8a.571.571 0 0 0 0-1.143zM16 16H5.714a.571.571 0 0 0 0
 1.143H16A.571.571 0 0 0 16 16zM2.286 17.143h1.143a.571.571 0 0 0
 0-1.143H2.286a.571.571 0 0 0 0 1.143zm17.143-3.429H16a.571.571 0 0 0
 0 1.143h3.429a.571.571 0 0 0 0-1.143zM9.143 14.857h4.571a.571.571 0 0
 0 0-1.143H9.143a.571.571 0 0 0 0 1.143zm-6.857 0h4.571a.571.571 0 0 0
 0-1.143H2.286a.571.571 0 0 0 0 1.143zM20.57 11.43H11.43a.571.571 0 0
 0 0 1.142h9.142a.571.571 0 0 0 0-1.142zM9.714 12a.571.571 0 0
 0-.571-.571H5.714a.571.571 0 0 0 0 1.142h3.429A.571.571 0 0 0 9.714
 12zm-7.428.571h1.143a.571.571 0 0 0 0-1.142H2.286a.571.571 0 0 0 0
 1.142zm19.428-3.428H16a.571.571 0 0 0 0 1.143h5.714a.571.571 0 0 0
 0-1.143zM2.286 10.286H8a.571.571 0 0 0 0-1.143H2.286a.571.571 0 0 0 0
 1.143zm13.143-2.857c0 .315.255.571.571.571h5.714a.571.571 0 0 0
 0-1.143H16a.571.571 0 0 0-.571.572zm-8.572-.572a.571.571 0 0 0 0
 1.143H8a.571.571 0 0 0 0-1.143H6.857zM2.286 8H4.57a.571.571 0 0 0
 0-1.143H2.286a.571.571 0 0 0 0 1.143zm16.571-2.857c0
 .315.256.571.572.571h1.142a.571.571 0 0 0 0-1.143H19.43a.571.571 0 0
 0-.572.572zm-1.143 0a.571.571 0 0 0-.571-.572H12.57a.571.571 0 0 0 0
 1.143h4.572a.571.571 0 0 0 .571-.571zm-15.428.571h8a.571.571 0 0 0
 0-1.143h-8a.571.571 0 0 0 0 1.143zm5.143-2.857c0
 .316.255.572.571.572h11.429a.571.571 0 0 0 0-1.143H8a.571.571 0 0
 0-.571.571zm-5.143.572h3.428a.571.571 0 0 0 0-1.143H2.286a.571.571 0
 0 0 0 1.143zm0-2.286H16A.571.571 0 0 0 16 0H2.286a.571.571 0 0 0 0
 1.143z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/prettier/prettier-logo/blo
b/06997b307e0608ebee2044dafa0b9429d6b5a103/images/prettier-icon-clean-'''

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
