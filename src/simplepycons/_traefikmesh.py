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


class TraefikMeshIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "traefikmesh"

    @property
    def original_file_name(self) -> "str":
        return "traefikmesh.svg"

    @property
    def title(self) -> "str":
        return "Traefik Mesh"

    @property
    def primary_color(self) -> "str":
        return "#9D0FB0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Traefik Mesh</title>
     <path d="m8.646 4.738.034.02 2.945 1.66a.66.66 0 0 0 .65
 0l2.92-1.644a.992.992 0 0 1 1.008 1.71l-.033.02-1.688.952a.33.33 0 0
 0 0 .574l4.555 2.57a.66.66 0 0 0 .65 0l2.815-1.59a.993.993 0 0 1 1.01
 1.71l-.035.02-1.585.89a.33.33 0 0 0 0 .578l1.594.897a.992.993 0 0
 1-.94 1.748l-.035-.02-2.826-1.591a.66.66 0 0 0-.65 0l-4.605
 2.595a.33.33 0 0 0 0 .575l1.905 1.072a.993.993 0 0 1-.94
 1.748l-.035-.018-3.133-1.767a.66.66 0 0 0-.65 0L8.416 19.23a.992.992
 0 0 1-1.006-1.71l.033-.02 1.93-1.088a.33.33 0 0 0
 0-.575l-4.564-2.572a.66.66 0 0 0-.65 0l-2.689 1.51a.993.993 0 0
 1-1.005-1.711l.034-.018 1.452-.817a.33.33 0 0 0
 0-.577l-1.45-.817a.992.992 0 0 1 .941-1.746l.033.018 2.685
 1.515a.66.66 0 0 0 .65 0l4.607-2.596a.33.33 0 0 0
 0-.576l-1.711-.963a.992.993 0 0 1 .94-1.748Zm2.977 4.324-4.609
 2.59a.33.33 0 0 0 0 .58l4.563 2.57a.66.66 0 0 0 .65
 0l4.606-2.595a.33.33 0 0 0 0-.577l-4.558-2.57a.66.66 0 0 0-.65 0z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/traefik/mesh/blob/ef03c40b
78c08931d47fdad0be10d1986f4e21bc/docs/content/assets/img/traefik-mesh-'''

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
