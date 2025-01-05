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


class IcingaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "icinga"

    @property
    def original_file_name(self) -> "str":
        return "icinga.svg"

    @property
    def title(self) -> "str":
        return "Icinga"

    @property
    def primary_color(self) -> "str":
        return "#06062C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Icinga</title>
     <path d="M13.8285.0086a2.122 2.122 0
 00-1.1546.4705c-.9134.7446-1.052 2.0897-.3057
 3.0038.1738.2135.382.3803.6085.5076l-1.9992
 4.1526c-1.3307-.5156-2.8925-.3242-4.0768.6411a4.1264 4.1264 0
 00-.2805.2538L4.3895
 7.2125c.124-.31.1253-.6679-.0326-.9913-.2979-.6072-1.0314-.859-1.6385-.561-.6079.2963-.8581
 1.0298-.561 1.637.2979.6063 1.029.8595
 1.637.5624.0991-.0483.1849-.1119.2642-.181l2.1846 1.7868c-1.1343
 1.4732-1.1567 3.5843.0712
 5.0876.2648.3253.5696.5978.9009.8193l-2.5067
 3.5945c-.5002-.3428-1.1085-.5336-1.7602-.4838-1.522.114-2.663
 1.4395-2.5482 2.9608.114 1.522 1.4403 2.663 2.9623 2.5483 1.522-.114
 2.6622-1.4396
 2.5482-2.9609-.0494-.6638-.3388-1.2483-.7658-1.6948l2.569-3.6836c1.1473.5518
 2.5128.5527 3.6718-.0505l1.444
 2.4117c-.1372.1332-.2392.3041-.2627.509-.0547.472.2836.899.7555.9529.471.054.8965-.2836.9528-.7555.054-.471-.2836-.898-.7554-.9528-.057-.007-.1097.0104-.1648.0148l-1.4856-2.4829c.072-.0512.1443-.1008.2137-.1573
 1.0746-.8777 1.584-2.1864
 1.493-3.4729l6.968-1.7186c.3257.484.888.7887 1.5108.742.9248-.0698
 1.6171-.8747
 1.548-1.7987-.07-.924-.8755-1.6156-1.7988-1.5464-.9247.0706-1.6163.874-1.5464
 1.7972.007.0956.0267.1876.049.2776l-6.8092
 1.68c-.1312-.6151-.4011-1.2094-.8252-1.7305-.3373-.4132-.7407-.7403-1.1799-.9854l2.017-4.1882c.6295.1558
 1.3211.0324 1.8625-.4081.9134-.7447
 1.0504-2.092.3058-3.0054-.466-.5709-1.1665-.8375-1.8492-.7762z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Icinga/icingaweb2/blob/293
021b2000e9d459387153ca5690f97e0184aaa/public/img/icinga-logo-compact.s'''

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
