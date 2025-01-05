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


class NucleoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nucleo"

    @property
    def original_file_name(self) -> "str":
        return "nucleo.svg"

    @property
    def title(self) -> "str":
        return "Nucleo"

    @property
    def primary_color(self) -> "str":
        return "#252B2D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nucleo</title>
     <path d="M12.025 0a3.868 3.868 0 00-1.964.525L1.354
 5.55V6.5h15.853a3.9 3.9 0 003.463-2.115L13.922.508A3.868 3.868 0
 0012.025 0zm9.81 5.072L13.91 18.801a3.9 3.9 0 00.1
 4.056l6.734-3.908a3.865 3.865 0 001.914-3.35V5.55l-.822-.477zM1.46
 7.848a3.9 3.9 0 00-.117.004l.017 7.787a3.868 3.868 0 001.946
 3.334L12.008 24l.824-.475-7.926-13.73A3.9 3.9 0 001.46 7.848zM11.992
 9.1a2.6 2.6 0 00-2.584 2.6 2.6 2.6 0 002.6 2.599 2.6 2.6 0 002.6-2.6
 2.6 2.6 0 00-2.6-2.6 2.6 2.6 0 00-.016 0Z" />
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
