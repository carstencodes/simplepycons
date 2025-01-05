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


class ArtifactHubIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "artifacthub"

    @property
    def original_file_name(self) -> "str":
        return "artifacthub.svg"

    @property
    def title(self) -> "str":
        return "Artifact Hub"

    @property
    def primary_color(self) -> "str":
        return "#417598"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Artifact Hub</title>
     <path d="M11.9999
 24.00044c-.617.0012-1.24209-.17217-1.78008-.50002l-7.50975-4.29263c-1.01763-.61684-1.64001-1.71772-1.64066-2.9077V7.72971c0-1.25305.63694-2.36948
 1.76008-3.01013L10.25041.47895c1.08003-.63867 2.41512-.63767
 3.49515.001l7.41975 4.23763c1.08007.59613 1.7714 1.7341 1.76266
 3.01013v8.58195c0 .96773-.44338 2.16388-1.63666 2.89856l-7.51074
 4.2922c-.56347.34395-1.19861.50002-1.78167.50002zm-.50002-21.34695L3.95513
 6.96224c-.2006.1567-.37906.36914-.37902.76747l.001
 8.67039c.03753.22045.11891.42808.37302.63459l7.55975
 4.31663c.26601.172.66403.21.98504
 0l7.51792-4.29663c.23173-.14844.37102-.38858.41002-.65359V7.72971c.0095-.29884-.13595-.5886-.37702-.76547L12.49993
 2.6525c-.39058-.23932-.7592-.15575-1.00004.001z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/artifacthub/hub/blob/b7df6
4e044687e5788d6e7e809539679eb9fe45a/web/public/static/media/logo/artif'''

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
