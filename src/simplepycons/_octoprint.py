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


class OctoprintIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "octoprint"

    @property
    def original_file_name(self) -> "str":
        return "octoprint.svg"

    @property
    def title(self) -> "str":
        return "OctoPrint"

    @property
    def primary_color(self) -> "str":
        return "#13C100"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OctoPrint</title>
     <path d="M3.942 4.613C2.424 5.987 1.107 7.473.476 9.71c-.634
 2.248-.585 5.094-.145 7.398.44 2.303 1.12 4.107 1.873
 5.83h13.179c-.31-.988-.761-1.967-1.446-3.237-.685-1.268-1.658-2.692-2.648-4.178-.99-1.486-1.985-3.077-1.851-4.472.094-.987.49-1.976
 1.492-2.76 1.16-.909 2.289-1.437 3.353-1.595 3.325-.496 6.422.601
 8.925 3.366.288.316.36.726.545
 1.127l.166-.653c.15-.589.088-1.359-.152-2.371-.243-1.029-.563-1.792-1.46-2.973-.893-1.176-2.467-2.322-4.48-3.226-1.5-.673-3.305-1-5.798-.879-2.522.124-5.494
 1.177-8.087 3.526Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/OctoPrint/OctoPrint/blob/5
3b9b6185781c07e8c4744a6e28462e96448f249/src/octoprint/static/img/mask.'''

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
