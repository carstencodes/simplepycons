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


class CastboxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "castbox"

    @property
    def original_file_name(self) -> "str":
        return "castbox.svg"

    @property
    def title(self) -> "str":
        return "Castbox"

    @property
    def primary_color(self) -> "str":
        return "#F55B23"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Castbox</title>
     <path d="M12 0c-.29 0-.58.068-.812.206L2.417
 5.392c-.46.272-.804.875-.804 1.408v10.4c0 .533.344 1.135.804
 1.407l8.77 5.187c.465.275 1.162.275 1.626
 0l8.77-5.187c.46-.272.804-.874.804-1.407V6.8c0-.533-.344-1.136-.804-1.408L12.813.206A1.618
 1.618 0 0012 0zm-.85 8.304c.394 0 .714.303.714.676v2.224c0
 .207.191.375.427.375s.428-.168.428-.375V9.57c0-.373.32-.675.713-.675.394
 0 .712.302.712.675v4.713c0 .374-.318.676-.712.676-.394
 0-.713-.302-.713-.676v-1.31c0-.206-.192-.374-.428-.374s-.427.168-.427.374v1.226c0
 .374-.32.676-.713.676-.394
 0-.713-.302-.713-.676v-1.667c0-.207-.192-.375-.428-.375-.235
 0-.427.168-.427.375v3.31c0 .373-.319.676-.712.676-.394
 0-.713-.303-.713-.676v-2.427c0-.206-.191-.374-.428-.374-.235
 0-.427.168-.427.374v.178a.71.71 0 01-.712.708.71.71 0
 01-.713-.708v-2.123a.71.71 0 01.713-.708.71.71 0 01.712.708v.178c0
 .206.192.373.427.373.237 0
 .428-.167.428-.373v-1.53c0-.374.32-.676.713-.676.393 0
 .712.303.712.676v.646c0 .206.192.374.427.374.236 0
 .428-.168.428-.374V8.98c0-.373.319-.676.713-.676zm4.562 2.416c.393 0
 .713.302.713.676v2.691c0 .374-.32.676-.713.676-.394
 0-.712-.303-.712-.676v-2.691c0-.374.319-.676.712-.676zm2.28
 1.368c.395 0 .713.303.713.676v.67c0 .374-.318.676-.712.676-.394
 0-.713-.302-.713-.675v-.67c0-.374.32-.677.713-.677Z" />
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
