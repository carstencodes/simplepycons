#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class FluxerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fluxer"

    @property
    def original_file_name(self) -> "str":
        return "fluxer.svg"

    @property
    def title(self) -> "str":
        return "Fluxer"

    @property
    def primary_color(self) -> "str":
        return "#4641D9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fluxer</title>
     <path d="M12 0c6.627 0 12 5.373 12 12s-5.373 12-12 12S0 18.627 0
 12 5.373 0 12 0M8.79 12.471q-1.092 0-2.078.493-.975.493-1.586
 1.575-.395.712-.52 1.726c-.078.626.448 1.135 1.079 1.135.645 0
 1.128-.543 1.284-1.17q.133-.531.429-.844.568-.6 1.435-.6.58 0
 1.061.289.482.279 1.254.954 1.178 1.038 2.078 1.51.9.46 1.993.461
 1.093 0 2.079-.493.985-.492
 1.596-1.575.404-.714.522-1.734c.072-.623-.455-1.127-1.083-1.127-.65
 0-1.134.549-1.307 1.176a2.1 2.1 0 0
 1-.382.774q-.535.665-1.468.665-.579
 0-1.05-.279-.46-.29-1.264-.964-1.19-.996-2.09-1.479a4 4 0 0
 0-1.982-.493M8.79 6q-1.092 0-2.078.493-.975.492-1.586
 1.575-.395.712-.52 1.726c-.078.625.448 1.135 1.079 1.135.645 0
 1.128-.543 1.284-1.17q.133-.533.429-.845.568-.6 1.435-.6.58 0
 1.061.29.482.278 1.254.953 1.178 1.04 2.078 1.51.9.462
 1.993.462t2.079-.493q.985-.493
 1.596-1.575.404-.716.522-1.734c.072-.624-.455-1.127-1.083-1.127-.65
 0-1.134.549-1.307 1.175a2.1 2.1 0 0
 1-.382.775q-.535.664-1.468.664-.579
 0-1.05-.278-.46-.29-1.264-.965-1.19-.996-2.09-1.478A4 4 0 0 0 8.79 6"
 />
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
