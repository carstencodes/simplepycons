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


class ArtixLinuxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "artixlinux"

    @property
    def original_file_name(self) -> "str":
        return "artixlinux.svg"

    @property
    def title(self) -> "str":
        return "Artix Linux"

    @property
    def primary_color(self) -> "str":
        return "#10A0CC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Artix Linux</title>
     <path d="M12 0L7.873 8.462l11.358 6.363zM6.626 11.018L.295
 24l18.788-7.762zm13.846 6.352l-5.926 3.402L23.706 24Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://gitea.artixlinux.org/artix/artwork/sr'''

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
