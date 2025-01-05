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


class CodecraftersIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "codecrafters"

    @property
    def original_file_name(self) -> "str":
        return "codecrafters.svg"

    @property
    def title(self) -> "str":
        return "CodeCrafters"

    @property
    def primary_color(self) -> "str":
        return "#171920"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CodeCrafters</title>
     <path d="M9.825 17.527a.111.111 0 0
 1-.107-.142l3.05-10.837a.111.111 0 0 1 .108-.081H14.2c.074 0
 .127.07.107.141l-3.063 10.838a.111.111 0 0
 1-.107.08H9.825Zm-2.146-2.732a.11.11 0 0
 1-.079-.033l-2.667-2.704a.111.111 0 0 1 0-.156L7.6 9.211a.111.111 0 0
 1 .08-.033h1.702c.1 0 .149.12.079.19l-2.534 2.534a.111.111 0 0 0 0
 .157l2.535 2.546c.07.07.02.19-.079.19H7.68Zm6.954 0a.111.111 0 0
 1-.079-.19l2.525-2.546a.111.111 0 0 0 0-.157l-2.524-2.535a.111.111 0
 0 1 .079-.19h1.692c.03 0 .058.013.078.034l2.68 2.69a.111.111 0 0 1 0
 .157l-2.68 2.704a.111.111 0 0 1-.078.033h-1.693ZM12 24C5.383 24 0
 18.617 0 12S5.383 0 12 0s12 5.383 12 12-5.383 12-12
 12Zm0-22.667C6.118 1.333 1.333 6.118 1.333 12S6.118 22.667 12 22.667
 22.667 17.882 22.667 12 17.882 1.333 12 1.333Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/codecrafters-io/frontend/b
lob/2f15115b73843fea57a412ce243ff1cedb5e69f7/public/assets/images/logo'''

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
